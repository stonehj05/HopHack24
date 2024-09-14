import sys
import re
import ast
import os
sys.path.insert(0, "..")
from image2text.utils import *
sys.path.remove("..")
api_key = os.environ.get('GPT_API_KEY')
def collect_resources(context) -> list:
    prompt = f"""
        You are an AI assistant trying to helping students learn. The context will show you the summarized content of a lecture students recently taken and the overall content of the course. Based on the information, provide students with some resources for additional learning in the url form. They can be readings, problems, or videos, are can be relate to the most recent lecture or more general course contents. Make sure your url are not hyper-link but raw url link to web page. Organize your answer in the form: Links: ["link1", "link2", ...]
        Context: {context}
    """
    response = gpt_api_call(prompt, 0.0, api_key).choice[0].message.content.strip()
    link_match = re.search(r'Links:\s*(\[[^\]]*\])', response)
    raw_response = link_match.group(1)
    links = ast.literal_eval(raw_response)
    return links