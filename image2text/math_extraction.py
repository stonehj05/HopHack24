from utils import *
import ast
import re
import os
api_key = get_openai_api_key()
def extract_information_from_math(image_paths:list[str]) -> dict:
    """
    Extracts mathematical formulas from an image containing handwritten text.
    Args:
        image_paths:

    Returns: A dictionary containing the mathematical formulas extracted from the image.

    """
    prompt = """You are a helpful assistant helping a person understanding some hand-write mathematical formulas. You 
    will read an image containing some handwriting on a board or on papers. From the image, identify if there is any 
    mathematical formulas in the written symbols. If there is any, convert them to some latex codes, keep the order 
    of hand-writing when converting, and only include converted latex code in your response. When you are converting, 
    you may identify the context of the formulas and modify latex codes based on the relevant topics. If there is no 
    mathematical formula, response with "No mathematical formula". Do not give any extra information."""
    response = gpt_api_call(prepare_multiple_image_message(prompt,image_paths), 0.0, api_key)
    if response[0:2] == "No":
        return []
    prompt = f""" You are a helpful assistant helping people organize a piece of latex code. You will read some piece 
    of latex source code. Identify different lines of latex code with each line representing a single formula or 
    equation. Make sure each line can compile by themselves. Organize the latex code in the following way: Codes: [
    "line1", "line2", ...]. Do not give any extra outputs. Latex codes: {response}
    """
    response = gpt_api_call(prepare_messages(prompt), 0.0, api_key)
    latex_code_match = re.search(r'Codes:\s*(\[[^\]]*\])', response)
    raw_response = latex_code_match.group(1)
    latex_codes = ast.literal_eval(raw_response)

    prompt = f""" You are a helpful assistant helping people understanding latex codes. You will read a list of latex 
    source codes. Each line of code represent a complete formula, equation or theorem. Based on the content and the 
    context, summarize what each line of code is trying to show. Organize your answer in the form Interpretations: [
    "Interpretation of line1", "Interpretation of line2", ...]. Make sure each line have a interpretation. Do not 
    give any extra contents. Latex code list: {raw_response}
    """
    response = gpt_api_call(prepare_messages(prompt), 0.0, api_key)
    interpretation_match = re.search(r'Interpretations:\s*(\[[^\]]*\])', response)
    raw_response = interpretation_match.group(1)
    interpretations = ast.literal_eval(raw_response)
    mathematical_formulas = {}
    for index, interpretation in enumerate(interpretations):
        mathematical_formulas[interpretation] = latex_codes[index]
    return mathematical_formulas


if __name__ == '__main__':
    image_path = ["./test_images/exact_equation_theorem.jpg", "./test_images/first_order_linear_ode.jpg"]
    print(extract_information_from_math(image_path))