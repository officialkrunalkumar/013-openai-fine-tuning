from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
api_key = os.getenv('APIKEY')

client = OpenAI(api_key=api_key)
if not api_key:
    raise ValueError("API key not found in environment variables.")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:zeni-revops::A8KqPcyb",
  messages=[
        {"role": "user", "content": "Can you explain the theory of relativity?"}
    ]
)

print(completion.choices[0].message.content)