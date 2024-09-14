# Usage Example:
import json
import os
from image2text.utils import prepare_image_message, gpt_api_call, prepare_followup_user_messages, \
    append_assistant_message

api_key = os.environ.get('GPT_API_KEY')
image_path = "path_to_your_image.jpg"
temperature = 0.7

# Step 1: Initial analysis
prompt = '''
You are an AI assistant designed to help students by analyzing images of classroom blackboards or whiteboards taken during lectures. The images should contain a diagram, graph, or illustration along with some labels. Your task is to extract the information from the image and provide relavent information based on the content. 


When provided with an image, please anaylze the content and extract the following information:

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
'''
followup_prompt = '''
Now, output the extracted information in the following JSON format, and include only the JSON data without any additional text, your output should be able to be directly parsed as JSON using a JSON parser in Python or any other programming language.

JSON Format:
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

def extract_information_from_image(image_path: str, context: str) -> dict:
    messages = prepare_image_message(prompt + context, image_path)
    response = gpt_api_call(messages, temperature, api_key)
    messages = append_assistant_message(messages, response)

    # Process the assistant's initial analysis (response)

    # Step 2: Request for JSON output
    messages = prepare_followup_user_messages(messages, followup_prompt)
    response = gpt_api_call(messages, temperature, api_key)

    # The final response should be the JSON output
    json_output = response['choices'][0]['message']['content']
    # parsing
    json_output = json.loads(json_output)
    return json_output