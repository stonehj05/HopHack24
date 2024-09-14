import sys
import re
import ast
import os
import copy
sys.path.insert(0, "..")
from image2text.utils import *
sys.path.remove("..")
api_key = ""
def generate_additional_learning(context): #context should integrate this lecture topic and course syllabus
    prompt = f"""
        You are a helpful assistant helping students learn some knowledge. The context of the recent lecture and the course in provided in the context section. Based on this inforation, generate the following questions to help students learn.
        1. 1-2 conceptual questions testing students' understanding of important concepts, words, or any other important things in the lecture.
        2. 1-2 basic questions requiring students to apply the new knowledge the learnt. The question should only require direct use of new knowledge.
        3. 1 hard question testing students' understanding of new knowledge.
        For each question generate, you need to solve them and know the answer to them. Generate the answer along with the questions. Organize your final response in this way:
        conceptual_questions: ["question1", "question2", ...]
        simple_questions: ["question1", "question2", ...]
        hard_question: ["question1", ...]
        conceptual_solution: ["solution for conceptual question 1", ...]
        simple_solution: ["solution for simple question 1", ...] 
        hard_solution: ["solution for hard question 1", ...]
        Context: {context}  
    """

    response = gpt_api_call(prompt, 0.0, api_key)
    match = re.search(r'conceptual_questions:\s*(\[[^\]]*\])', response)
    raw_response = match.group(1)
    conceptual_questions = ast.literal_eval(raw_response)

    match = re.search(r'simple_questions:\s*(\[[^\]]*\])', response)
    raw_response = match.group(1)
    simple_questions = ast.literal_eval(raw_response)

    match = re.search(r'hard_question:\s*(\[[^\]]*\])', response)
    raw_response = match.group(1)
    hard_questions = ast.literal_eval(raw_response)

    match = re.search(r'conceptual_solution:\s*(\[[^\]]*\])', response)
    raw_response = match.group(1)
    conceptual_solutions = ast.literal_eval(raw_response)

    match = re.search(r'simple_solution:\s*(\[[^\]]*\])', response)
    raw_response = match.group(1)
    simple_solutions = ast.literal_eval(raw_response)

    match = re.search(r'hard_solution:\s*(\[[^\]]*\])', response)
    raw_response = match.group(1)
    hard_solutions = ast.literal_eval(raw_response)

    return conceptual_questions, simple_questions, hard_questions, conceptual_solutions, simple_solutions, hard_solutions