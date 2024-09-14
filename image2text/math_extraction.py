from utils import *

def math_extraction(image_path):
    prompt = """
        You are a helpful assistant helping a person understanding some hand-write mathematical formulas. You will read an image containing some handwriting on a board or on papers. From the image, identify if there is any mathematical formulas in the written symbols. If there is any, convert them to some latex codes, and only include converted latex code in your response. If there is no mathematical formula, response with "No mathematical formula". Do not give any extra information.
    """
    
