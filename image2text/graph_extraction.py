import json

from image2text.utils import *

api_key = get_openai_api_key()


# Step 1: Initial analysis
prompt = '''
You are an AI assistant designed to help students by analyzing images of classroom blackboards or whiteboards taken during lectures. The images should contain a diagram, graph, or illustration along with some labels. Your task is to extract the information from the image and provide relavent information based on the content. 


When provided with an image, please anaylze the content and extract the following information:

1. **Transcription and Extraction**:
   - **Text**: Accurately transcribe all written text in the image.
   - **Equations**: Identify and transcribe all mathematical equations or expressions, formatting them using LaTeX syntax where appropriate.
   - **Diagrams and Graphs**: Detect any diagrams, graphs, or illustrations, and provide detailed descriptions of their components and what they represent.

2. **Explanation and Contextualization**:
   - **Clarify Concepts**: Provide brief explanations or definitions for technical terms, symbols, or concepts that appear in the content.
   - **Elaborate on Visuals**: For diagrams and graphs, explain their purpose, the relationships they depict, and any trends or patterns.
   - **Connect Ideas**: Highlight connections between different parts of the content, such as how an equation relates to a graph or how a concept fits into the broader topic.

3. **Enhancements**:
   - **Formatting**: Use markdown formatting to enhance readability (e.g., bold for key terms, italics for emphasis, code blocks for equations).
   - **Summarization**: At the end of the notes, provide a brief summary of the main points covered in the image.
'''
followup_prompt = '''
Now, output the extracted information in the following JSON format, and include only the JSON data without any additional text, your output should be able to be directly parsed as JSON using a JSON parser in Python or any other programming language.
Start your answer with the open bracket "{", and end it with a closing bracket "}". Please escape any special characters in the output, like the blackslash "\" should be output as "\\".
{
  "Diagrams": [
    {
      "Description": "<Detailed description of the diagram or graph>",
      "Summary": "<Brief summary of the diagram's content that would be helpful when listed alongside the diagram>",
      "Interpretation": "<Explanation of what it represents and its significance>",
      "Text": "<A paragraph recording the transcribed and organized text labels and markings on this diagram>",
      "Equations": ["<List of equations involved in the equation in LaTeX format>"],"
      "Related Concepts": ["<List of related concepts or topics covered in the diagram>"]
      "Reillustration": "<Search the internet and find a webpage containing similar image illustrating diagram or graph, paste the link here, it should be a well known site like wikipedia.>"
    }
    // Repeat for additional diagrams
  ]
}'''


def extract_information_from_graph(image_paths: list[str], context: str = "") -> dict:
    messages = prepare_multiple_image_message(prompt + context, image_paths)
    output = get_default_chat_response(messages, followup_prompt, temperature=0.7, api_key=api_key)
    print("graph:", output)
    # parsing
    try:
        json_output = json.loads(output)
    except json.JSONDecodeError as e:
        print(f"An JSONDecodeError occurred: {e}")
        return {}
    return json_output


if __name__ == '__main__':
    image_path = ["../img/test_graph.jpeg"]
    context = ""
    extracted_info = extract_information_from_graph(image_path, context)
    print(extracted_info)
