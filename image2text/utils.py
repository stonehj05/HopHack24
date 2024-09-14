import base64
import openai
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

def gpt_api_call(prompt: str, temperature: float, api_key: str) -> dict:
    """
    Calls the OpenAI GPT API with the given prompt and temperature.

    Args:
        prompt (str): The system prompt to guide the AI's behavior.
        temperature (float): Sampling temperature for the response.
        api_key (str): Your OpenAI API key.

    Returns:
        dict: The API response containing the AI's completion.
    """
    # Initialize the OpenAI client using the helper function
    client = get_openai_client(api_key)

    # Prepare the message payload using the helper function
    messages = prepare_messages(prompt)

    try:
        # Make the API call to OpenAI's Chat Completion endpoint
        response = client.chat.completions.create(
            model="gpt-4",          # Ensure the model name is correct
            messages=messages,
            temperature=temperature
        )
        return response
    except openai.error.OpenAIError as e:
        # Handle API errors gracefully
        print(f"An error occurred: {e}")
        return {}

def gpt_api_call_with_image(prompt: str, image_path: str, temperature: float, api_key: str) -> dict:
    """
    Calls the OpenAI GPT API with the given prompt, image, and temperature.

    Args:
        prompt (str): The system prompt to guide the AI's behavior.
        image_path (str): The path to the image file.
        temperature (float): Sampling temperature for the response.
        api_key (str): Your OpenAI API key.

    Returns:
        dict: The API response containing the AI's completion.
    """
    # Initialize the OpenAI client using the helper function
    client = get_openai_client(api_key)

    # Prepare the image message payload using the helper function
    messages = prepare_image_message(prompt, image_path)

    try:
        # Make the API call to OpenAI's Chat Completion endpoint
        response = client.chat.completions.create(
            model="gpt-4",          # Ensure the model name is correct
            messages=messages,
            temperature=temperature
        )
        return response
    except openai.error.OpenAIError as e:
        # Handle API errors gracefully
        print(f"An error occurred: {e}")
        return {}
