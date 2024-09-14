from image2text.utils import *
import ast
import re
import json
import os

api_key = get_openai_api_key()
prompt = """
        You are an AI assistant designed to help students by analyzing images of classroom blackboards or whiteboards taken during lectures. The images may contain handwritten text, diagrams, graphs, equations, and other visual elements related to the lecture content.

        **Your tasks are as follows:**

        1. **Transcription and Extraction**:
        - **Text**: Accurately transcribe all written text in the image.
        - **Equations**: Identify and transcribe all mathematical equations or expressions, formatting them using LaTeX syntax where appropriate.
        - **Diagrams and Graphs**: Detect any diagrams, graphs, or illustrations, and provide detailed descriptions of their components and what they represent.

        2. **Organization**:
        - **Structured Notes**: Organize the extracted information into clear, structured notes using headings, subheadings, bullet points, and numbered lists as appropriate.
        - **Sections**: Divide the content into logical sections that mirror the flow of the lecture, such as "Introduction," "Key Concepts," "Examples," "Conclusion," etc.

        3. **Explanation and Contextualization**:
        - **Clarify Concepts**: Provide brief explanations or definitions for technical terms, symbols, or concepts that appear in the content.
        - **Elaborate on Visuals**: For diagrams and graphs, explain their purpose, the relationships they depict, and any trends or patterns.
        - **Connect Ideas**: Highlight connections between different parts of the content, such as how an equation relates to a graph or how a concept fits into the broader topic.

        4. **Enhancements**:
        - **Formatting**: Use markdown formatting to enhance readability (e.g., bold for key terms, italics for emphasis, code blocks for equations).
        - **Summarization**: At the end of the notes, provide a brief summary of the main points covered in the image.

    """
followup_prompt = r'''Now, output the extracted information in the following JSON format, and include only the JSON 
data without any additional text, start with an open bracket "{",your output should be able to be directly parsed as 
JSON using a JSON parser in Python or any other programming language. Please escape any special characters in the output, like the blackslash "\" should be output as "\\".

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
        // Repeat for additional sections
    ],
    "Summary": "<Brief summary of the main points>"
}
'''


def extract_information_from_handnotes(image_paths: list[str], context: str) -> dict:
    messages = prepare_multiple_image_message(prompt + context, image_paths)
    output = get_default_chat_response(messages, followup_prompt, temperature=0.7, api_key=api_key)
    print(output)
    # parsing
    try:
        json_output = json.loads(output)
    except json.JSONDecodeError as e:
        print(f"An JSONDecodeError occurred: {e}")
        return {}
    return json_output


# def handnotes_extraction(image_path):
#     response = gpt_api_call(prompt, 0.0, api_key, image_path)
#     note = ast.literal_eval(response)
#     json.dump(note, "note.json", indent=4)

if __name__ == '__main__':
    context = ""
    image_path = ['./test_images/first_order_linear_ode.jpg', './test_images/exact_equation_theorem.jpg']
    output = extract_information_from_handnotes(image_path, context)
    print(output)
    # Save the output to a JSON file
    with open('handnote_output.json', 'w') as f:
        json.dump(output, f, indent=4)
