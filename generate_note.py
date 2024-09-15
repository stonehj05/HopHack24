from image2text.utils import *
import os
import json
from image2text import math_extraction
from image2text import graph_extraction
from image2text import handnotes_extraction
from transcription_segmentation import post_process_transcription_data
from voice2text.voice_text import transcribe_audio_files

api_key = get_openai_api_key()


def generate_note(board_notes, audio_transcript, hand_notes, context="", course_name="default_course", lecture_name="default_lecture", note_name="note.md"):
    # Create the directory structure /data/<course_name>/<lecture_name> if it doesn't exist
    lecture_dir = os.path.join("data", course_name, lecture_name)
    os.makedirs(lecture_dir, exist_ok=True)

    # if note exist skip the process and read value off the file
    if os.path.exists(os.path.join(lecture_dir, note_name)) and os.path.exists(os.path.join(lecture_dir, "transcription.txt")):
        print("Note and transcription already exist, reading from file")
        with open(os.path.join(lecture_dir, note_name), "r") as file:
            note = file.read()
        with open(os.path.join(lecture_dir, "transcription.txt"), "r") as file:
            transcription = file.read()
        with open(os.path.join(lecture_dir, "diagrams.json"), "r") as file:
            diagrams = json.load(file)
        
        post_process_transcription_data(transcription, note, diagrams, course_name, lecture_name)
        return


    transcription = transcribe_audio_files(audio_transcript)
    # loop over the transcription and join them
    transcription = " ".join(transcription)
    print(f"Transcription: {transcription}")

    formulas = math_extraction.extract_information_from_math(board_notes)
    print(f"Formulas: {formulas}")
    diagrams = graph_extraction.extract_information_from_graph(board_notes)
    print(f"Diagrams: {diagrams}")
    hand_writings = handnotes_extraction.extract_information_from_handnotes(hand_notes)
    print(f"Handwriting: {hand_writings}")


    # Save the extracted information into the appropriate files within the lecture directory
    # with open(os.path.join(lecture_dir, "formulas.json"), "w") as file:
    #     json.dump(formulas, file, indent=4)
    with open(os.path.join(lecture_dir, "diagrams.json"), "w") as file:
        json.dump(diagrams, file, indent=4)
    with open(os.path.join(lecture_dir, "handwriting.json"), "w") as file:
        json.dump(hand_writings, file, indent=4)
    with open(os.path.join(lecture_dir, "transcription.txt"), "w") as file:
        file.write(str(transcription))

    prompt = r"""You are an adept note taker, and your task is to help a student organize the notes from a lecture. 
    You will read several things: 
    Context: the context of the course material and the topics for the lecture 
    Formulas: mathematical formulas the professor wrote on the board with explanations of their purposes 
    Diagram: descriptions of the graphs the professor drew on the board 
    Handwriting: the original notes taken by the student 
    Transcription: the lecture transcription given by the professor

    With all the information, your goal is to generate a complete note of the lecture integrating each part of 
    information. You should provide a brief summary of the lecture's contents at the beginning, then provide an 
    outline for the lecture at the beginning of the note. Finally, you should generate a detailed note following the 
    outline, with detailed explanations based on the lecture transcript, formulas, and diagrams. Your output should be in 
    markdown format. Only include note content in your output, without any additional information or summary.
    Here is an example of the output format:
    # <Title of the lecture>
    ## Summary
    <Brief summary of the lecture content>
    ## Outline
    <Numbered list (with nested unnumbered lists) of the main topics covered in the lecture>
    ## Detailed Notes
    <Detailed notes for each topic, with explanations, formulas, and diagrams, matching the structure of the outline>
    ## Diagrams & Related Resources
    <For each diagram, generate a hyperlink with description, using the reillustration field for each diagram>
    
    Please notice the following:
    - The note should be well-organized, with clear headings and subheadings as listed in the outline.$[ f(n) = O(g(n)) \iff \exists C, N_0 \in \mathbb{R}, \text{ s.t. } \forall N \geq N_0, |f(N)| \leq C \cdot g(N) ]$
    - Whenever there is latex code, suround it with a single $ symbol. NOT the \( \) symbol. the $$ $$ math block is prohibited. Do not escape the \ symbol in the output. Never use multiple lines for a single formula. Always treat it inline. Long math formula can go on as a single line by itself.
        - Example: For $x \in \mathbb{R}$, We know that $x=2$ is a solution to the equation $x^2 - 4 = 0$.
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
    with open(os.path.join(lecture_dir, note_name), "w") as file:
        file.write(response)
    # return transcription, response, diagrams
    print("Post processing transcription data")
    post_process_transcription_data(transcription, response, diagrams, course_name, lecture_name)

if __name__ == '__main__':

    # TODO: automatically read it from the folder. Should encapsulate this process with a function main_process(lecture_directory)
    board_notes_paths = ['./img/board_1.jpg', './img/board_2.jpg', './img/board_3.jpg']
    hand_notes_paths = ['./img/handnote.jpg']
    transcription_paths = ['./test_data/data_structure/lecture_audio.mp3']
    context = "This is a lecture about binary search tree in a data structure class."
    generate_note(board_notes_paths, transcription_paths, hand_notes_paths, context)

    # # Optional: Gnerate and store segmentation, flashcard, and questions.
    # print("Post processing transcription data")
    # post_process_transcription_data(transcription,note_text=note_text,graph_data=graph_data)
