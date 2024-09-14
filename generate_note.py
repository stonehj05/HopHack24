from image2text.utils import *
import ast
from image2text import math_extraction
from image2text import graph_extraction
from image2text import handnotes_extraction
from voice2text.voice_text import transcribe_audio_files

api_key = get_openai_api_key()
def generate_note(board_notes, audio_transcript, hand_notes, context = ""):
    formulas = math_extraction.extract_information_from_math(board_notes)
    print(f"Formulas: {formulas}")
    diagrams = graph_extraction.extract_information_from_graph(board_notes)
    print(f"Diagrams: {diagrams}")
    hand_writings = handnotes_extraction.extract_information_from_handnotes(hand_notes)
    print(f"Handwriting: {hand_writings}")
    transcription = transcribe_audio_files(audio_transcript)
    print(f"Transcription: {transcription}")
    prompt = r"""You are a adept note taker, and your task is to help a student organizing the notes in a lecture. 
    You will read several things: 
    Context: the context of the course material and the topics for the lecture 
    Formulas: mathematical formulas professor written on the board with explaination of their purposes 
    Diagram:describing the graphs professor draw on the board Handwriting: the original notes taken by the students. 
    
    With all the information, reorganize and process them into a high quality learning note. You should respect the 
    materials in the original notes and make sure the final note is clear and easy to understand. Your output should be in markdown format. 
    
    First start with an Summary paragraph of this lecture. Then generate an outline for the note that includes all the topics and subtopics.
    without fine-grained details. Afterwards start generating"""
    prompt += f"""
        Inputs:
        Context: {context}
        Formulas: {formulas}
        Diagrams: {diagrams}
        Hand_writing: {hand_writings}
        Transcription: {transcription}
    """
    response = gpt_api_call(prepare_messages(prompt), 0.0, api_key)
    print("\n\n\n===Final Note===\n\n\n")
    print(response)

if __name__ == '__main__':
    board_notes = ['./img/test_graph.jpeg']
    hand_notes = ['./image2text/test_images/first_order_linear_ode.jpg', './image2text/test_images/exact_equation_theorem.jpg']
    transcription = ['./voice2text/Harry.mp3']
    context = "This is a lecture on calculus and linear algebra"
    generate_note(board_notes, transcription, hand_notes, context)