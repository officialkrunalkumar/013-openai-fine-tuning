from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('APIKEYP')

client = OpenAI(api_key=api_key)

if not api_key:
    raise ValueError("API key not found in environment variables.")

try:
    response = client.models.list()
    #ft:gpt-4o-mini-2024-07-18:zeni-revops:churn-reason-dictionary-2:A8KT8btt
    #ft:gpt-4o-mini-2024-07-18:zeni-revops:myfinetunedchatwithvalidation:A87Wx5pd
    print(response)
    response = client.chat.completions.create(model="ft:gpt-4o-mini-2024-07-18:zeni-revops:churn-reason-dictionary-2:A8KT8btt",
                                              
    messages=[
        {"role": "user", "content": "FitSwoop Inc. churned due to a transition to an in-house team, indicating dissatisfaction with the support received, especially from their controller (Ticket Notes). They struggled with dashboard navigation and lacked effective help for reporting (Company Notes)."}
    ])

    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
