from image2text.utils import *
import ast
from image2text import math_extraction
from image2text import graph_extraction
from image2text import handnotes_extraction
api_key = get_openai_api_key()
def generate_note(board_notes, audio_transcript, hand_notes, context):
    formulas = math_extraction.extract_information_from_math(board_notes)
    diagrams = graph_extraction.extract_information_from_graph(board_notes)
    hand_writings = handnotes_extraction.extract_information_from_handnotes(hand_notes)
    prompt = r"""
    You are a helpful AI assistant helping a student organizing the notes in a lecture. You will read several things: 
    Context: the context of the course material and the topics for the lecture
    Formulas: mathematical formulas professor written on the board with explaination of their purposes Diagram:describing the graphs professor draw on the boad
    Handwriting: the original notes taken by the students. 
    With all the information, add information to students' notes or reorganize. You need to match the information from formulas and diagram with corresponding missing section in students' notes, organize information in logical order, and generate a note in the following JSON form:
    JSON Format:
    {
        "Title": "<If a title or topic is identified, include it here>",
        "Content": [
            {
            "SectionTitle": "<Title of the section>",
            "Text": "<Transcribed and organized text for this section>",
            "Equations": ["<List of equations in LaTeX format>"],
            "Diagrams": [
                {
                "Description": "<Detailed description of the diagram or graph>",
                "Interpretation": "<Explanation of what it represents and its significance>"
                }
            ]
            }
            Repeat for additional sections
        ],
        "Summary": "<Brief summary of the main points>"
    }
    """
    prompt += f"""
        Inputs:
        Context: {context}
        Formulas: {formulas}
        Diagrams: {diagrams}
        Hand_writing: {hand_writings}
    """
    response = gpt_api_call(prompt, 0.0, api_key)
    result = json.loads(response)
    print(result)

    