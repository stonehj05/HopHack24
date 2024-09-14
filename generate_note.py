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
    with open("script.txt", "r") as file: #temporary
        transcription = file.read()
    print(f"Transcription: {transcription}")
    prompt = r"""You are a adept note taker, and your task is to help a student organizing the notes in a lecture. 
    You will read several things: 
    Context: the context of the course material and the topics for the lecture 
    Formulas: mathematical formulas professor written on the board with explaination of their purposes 
    Diagram: describing the graphs professor draw on the board 
    Handwriting: the original notes taken by the students. 
    Transcription: the lecture transcription given by the professor
    
    With all the information, your goal is to generate a complete note of the lecture integrating each part of information. You should provide a brief summary of the lecture's contents at the beginning, then provide an outline for the lecture at the beginning of the note. Finally, you should generate a detailed note following the outline, with detailed explaination based on lecture transcript, formulas and diagrams. Your output should be in markdown format. 
    """
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
    board_notes = ['./img/board_1.jpg', './img/board_2.jpg', './img/board_3.jpg']
    hand_notes = ['./img/handnote.jpg']
    transcription = ['./voice2text/Harry.mp3']
    context = "This is a lecture about binary search tree in a data structure class."
    generate_note(board_notes, transcription, hand_notes, context)