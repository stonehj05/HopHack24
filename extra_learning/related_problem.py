import sys
import re
import ast
import os
sys.path.insert(0, "..")
from image2text.utils import *
sys.path.remove("..")
api_key = os.environ.get('GPT_API_KEY')
def collect_problems(context) -> list:
    prompt = f"""
        You are an AI assistant trying to helping students learn. The context will show you the summarized content of a lecture students recently taken. Based on the information, search the internet for some additional pratice problem for to test whether students' understand the material and credit the source. If there is a mathematical formula in the question, use latex codes to show the problem. For sources if links are present, show them in plain link. Organize your answer in the following way: Questions: ["question1", "question2", ...], Sources: ["source for question1", "source for question2", ...]
        Context: {context}
    """
    response = gpt_api_call(prompt, 0.0, api_key).choice[0].message.content.strip()
    question_match = re.search(r'Questions:\s*(\[[^\]]*\])', response)
    raw_response = question_match.group(1)
    questions = ast.literal_eval(raw_response)
    source_match = re.search(r'Sources:\s*(\[[^\]]*\])', response)
    raw_response = source_match.group(1)
    sources = ast.literal_eval(raw_response)
    return questions, sources