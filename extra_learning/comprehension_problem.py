import sys
import re
import ast
import os
sys.path.insert(0, "..")
from image2text.utils import *
sys.path.remove("..")
api_key = os.environ.get('GPT_API_KEY')
def generate_problems(context):
    prompt = f"""
        You are an AI assistant trying to helping students learn. The context will show you the summarized content of a lecture students recently taken. Based on the information, come up with some questions testing students' understanding of basic concepts. The questions are for comprehension instead of computation. You should generate 1 to 3 questions. Organize your question in the following form: Questions: ["question1", "question2", "question3"]
        Context: {context}
    """
    response = gpt_api_call(prompt, 0.0, api_key).choice[0].message.content.strip()
    question_match = re.search(r'Questions:\s*(\[[^\]]*\])', response)
    raw_response = question_match.group(1)
    questions = ast.literal_eval(raw_response)
    return questions