import os
from dotenv import load_dotenv
from .utils import gpt_api_call

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Get the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OpenAI API key not found. Please add it to your .env file.")
        return

    # Define your system prompt
    system_prompt = "You are an AI assistant that helps with Python programming questions."

    # Define the temperature for the AI's responses
    temperature = 0.7

    # Make the API call
    response = gpt_api_call(prompt=system_prompt, temperature=temperature, api_key=api_key)

    # Check if the response is not empty
    if response:
        # Extract and print the AI's reply
        ai_message = response.get("choices", [])[0].get("message", {}).get("content", "")
        print("AI Response:", ai_message)
    else:
        print("Failed to get a response from the OpenAI API.")

if __name__ == "__main__":
    main()
