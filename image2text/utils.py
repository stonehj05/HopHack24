import base64
import json
import os

import dotenv
import matplotlib.pyplot as plt
import openai

def get_openai_api_key():
    dotenv.load_dotenv()
    return os.getenv("OPENAI_API_KEY")

import requests
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
        {"role": "user", "content": "Please provide your input here."}
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

def gpt_api_call(messages: list, temperature: float, api_key: str) -> str:
    """
    Calls the OpenAI GPT API with the given messages and temperature.
    Returns: str: The API response string.
    """
    # Initialize the OpenAI client using the helper function
    client = get_openai_client(api_key)

    try:
        # Make the API call to OpenAI's Chat Completion endpoint
        response = client.chat.completions.create(
            model="gpt-4o",          # Ensure the model name is correct
            messages=messages,
            temperature=temperature
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

def get_default_chat_response(initial_message:dict, follow_up_prompt:str, temperature=0.7, api_key="") -> dict:
    # Process the assistant's initial analysis (response)
    messages = initial_message
    response = gpt_api_call(messages, temperature, api_key)
    messages = append_assistant_message(messages, response)


    # Step 2: Request for JSON output or any other followup
    messages = prepare_followup_user_messages(messages, follow_up_prompt)
    output = gpt_api_call(messages, temperature, api_key)


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