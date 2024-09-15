import openai
from image2text.utils import *
api_key = get_openai_api_key()

def generate_response(question, context=""):
    prompt = """
        You are a helpful AI assistant helping students to answer there questions. You will read context about the course the student is taking and the recent lecture in the course. The context include two parts
        1. The content of course syllabus
        2. The lecture notes for the lecture
        Based on these information and your own knowledge, answer students' questions. If you have to generate latex codes for mathematical formulas, make sure they can get compiled. Include answer and detailed explanations for students' questions. Do not include any extra contents.
    """
    response = gpt_api_call(prompt, 0.0, api_key)
    return response
