# Usage Example:
from image2text.utils import prepare_image_message, gpt_api_call

api_key = "YOUR_API_KEY"
image_path = "path_to_your_image.jpg"
temperature = 0.7

# Step 1: Initial analysis
prompt = '''You are an AI assistant designed to extract and organize information from images of handwritten notes or blackboard content, including text, equations, and diagrams, to aid students in their note-taking process.

When provided with an image, please:

1. **First**, analyze and discuss the content of the image, identifying key points, equations, and diagrams.

2. **Then**, when requested, output the extracted information in the following JSON format, and include only the JSON data without any additional text:

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
}'''

messages = prepare_image_message(prompt, image_path)
response = gpt_api_call(messages, temperature, api_key)

# Process the assistant's initial analysis (response)

# Step 2: Request for JSON output
messages = prepare_followup_messages(messages)
response = gpt_api_call(messages, temperature, api_key)

# The final response should be the JSON output
json_output = response['choices'][0]['message']['content']
print(json_output)
