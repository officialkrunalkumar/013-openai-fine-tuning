from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('APIKEY')

client = OpenAI(api_key=api_key)
if not api_key:
    raise ValueError("API key not found in environment variables.")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:zeni-revops:churngpt:A8UdFXbe",
  messages=[
        {"role": "user", "content": "Customer has indicated that they are moving to a competitor due to better service offerings."}
    ]
)

print(completion.choices[0].message.content)