from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv('APIKEY')

client = OpenAI(api_key=api_key)

# Check if the API key is loaded correctly
if not api_key:
    raise ValueError("API key not found in environment variables.")

# Set the OpenAI API key

try:
    # List available models
    response = client.models.list()

    # Print model IDs and names
    # for model in response.data:
    #     print(f"Model ID: {model['id']}, Name: {model.get('name', 'No Name')}")

    # Make a request to the fine-tuned model
    response = client.chat.completions.create(model="ft:gpt-4o-mini-2024-07-18:zeni-revops:myfinetunedchatwithvalidation:A87Wx5pd",  # Replace with your fine-tuned model ID
    messages=[
        {"role": "user", "content": "What's the weather like today?"}
    ])

    # Print the assistant's response
    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
