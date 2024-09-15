import base64
import json
import os
import PyPDF2
import dotenv
import matplotlib.pyplot as plt
import openai
import docx
import requests
import zipfile
import fitz
from PIL import Image
from io import BytesIO


def get_openai_api_key():
    dotenv.load_dotenv()
    return os.getenv("OPENAI_API_KEY")


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_openai_client(api_key: str) -> openai.OpenAI:
    """
    Initializes and returns the OpenAI client.

    Args:
        api_key (str): Your OpenAI API key.

    Returns:
        openai.OpenAI: An instance of the OpenAI client.
    """
    return openai.OpenAI(api_key=api_key)


def prepare_messages(prompt: str) -> list:
    """
    Prepares the message payload for the OpenAI Chat Completion API.

    Args:
        prompt (str): The system prompt to guide the AI's behavior.

    Returns:
        list: A list of message dictionaries.
    """
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Please provide your input here."} #TODO: confirm if we need this
    ]


def prepare_image_message(prompt: str, image_path: str) -> dict:
    """
    Prepares the image message payload for the OpenAI Chat Completion API.

    Args:
        image_path (str): The path to the image file.

    Returns:
        dict: The image message dictionary.
    """
    # Encode the image as a base64 string
    image_data = encode_image(image_path)

    # Prepare the image message payload
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": [
            {"type": "text", "text": "Input image"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
        ]}
    ]



def prepare_multiple_image_message(prompt: str, image_paths: list) -> dict:
    """
    Prepares the image message payload for the OpenAI Chat Completion API,
    accepting multiple images and adding them to the context.

    Args:
        prompt (str): The prompt for the system.
        image_paths (list): A list of paths to image files.

    Returns:
        dict: The image message dictionary with multiple images.
    """
    # Prepare the initial context with the system prompt
    message_payload = [{"role": "system", "content": prompt}]

    # Loop through the list of image paths and encode each image
    for image_path in image_paths:
        image_data = encode_image(image_path)  # Function that encodes image to base64

        # Add the image and accompanying text to the user message
        message_payload.append(
            {"role": "user", "content": [
                {"type": "text", "text": f"Input image {image_paths.index(image_path) + 1}"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
            ]}
        )

    return message_payload


def gpt_api_call(messages: dict, temperature: float, api_key: str, json_mode = False) -> str:
    """
    Calls the OpenAI GPT API with the given messages and temperature.
    Returns: str: The API response string.
    """
    # Initialize the OpenAI client using the helper function
    client = get_openai_client(api_key)

    try:
        # Make the API call to OpenAI's Chat Completion endpoint
        response = client.chat.completions.create(
            model="gpt-4o",  # Ensure the model name is correct
            messages=messages,
            temperature=temperature,
            response_format={"type": "json_object"} if json_mode else {"type": "text"}
        )
        return response.choices[0].message.content.strip()
    except openai.OpenAIError as e:
        # Handle API errors gracefully
        print(f"An error occurred: {e}")
        return {}


def latex_rendering(latex_source_code, output_file_path):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.text(0.5, 0.5, latex_source_code, fontsize=16, ha='center', va='center')
    plt.savefig(output_file_path, bbox_inches='tight', dpi=300)


def append_assistant_message(messages: list, assistant_msg: str) -> list:
    messages.append({"role": "assistant", "content": assistant_msg})
    return messages


def prepare_followup_user_messages(messages: list, followup_user_msg: str) -> list:
    messages.append({"role": "user", "content": followup_user_msg})
    return messages


def get_default_chat_response(initial_message: dict, follow_up_prompt: str, temperature=0.7, api_key="") -> dict:
    # Process the assistant's initial analysis (response)
    messages = initial_message
    response = gpt_api_call(messages, temperature, api_key)
    messages = append_assistant_message(messages, response)

    # Step 2: Request for JSON output or any other followup
    messages = prepare_followup_user_messages(messages, follow_up_prompt)
    output = gpt_api_call(messages, temperature, api_key, json_mode=True)

    return output


def check_url(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

def parse_latex(text):
    ans = []
    parsed_data = json.loads(text)
    for line in parsed_data:
        ans.append(line)
    return ans

def read_pdf(pdf_path):
    with open(pdf_path, "rb"):
        reader = PyPDF2.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    print(num_pages)
    # Extract text from each page
    text = ""
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()

        print(text)

def read_docx(file_path):
    doc = docx.Document(file_path)
    doc_text = []
    for paragraph in doc.paragraphs:
        doc_text.append(paragraph.text)

    return '\n'.join(doc_text)

def read_zip_images(zip_file_path, image_path): #export all zipped images to data directory, and return a list of link pointing to those images
    output_list = []
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                with zip_ref.open(file_name) as img_file:
                    image = Image.open(BytesIO(img_file.read()))
                    image_output_path = os.path.join(image_path, os.path.basename(file_name))  # Save using base file name
                    image.save(image_output_path)
                    output_list.append(image_output_path)
    return output_list

def read_pdf_images(pdf_path, output_dir, image_format='png'):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_list = []
    # Loop through each page in the PDF
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_num)
        
        # Render page to an image (use a zoom factor for higher resolution)
        pix = page.get_pixmap()
        
        # Save image to output directory
        output_file_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        pix.save(output_file_path)
        output_list.append(output_file_path)
    
    pdf_document.close()
    return output_list
    
if __name__ == "__main__":
    read_pdf_images("110.302DiffEqSyllabus.pdf", ".")