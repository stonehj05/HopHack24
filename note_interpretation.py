from openai import OpenAI
import base64
client = OpenAI(
    api_key = ""
)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def gpt_api_call(prompt, temperature, image_path): #this function might not be valid for few-shots implementation
    image_data = encode_image(image_path)
    response = client.chat.completions.create(
        messages = [
            {"role": "system", "content": prompt}
        ],
        model="gpt-4o",
        temperature = temperature
    )
