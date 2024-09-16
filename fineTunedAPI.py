import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

# Example of making a request to the fine-tuned model
response = openai.ChatCompletion.create(
    model="ft:gpt-4-xyz123",  # Replace with your fine-tuned model ID
    messages=[
        {"role": "user", "content": "What's the weather like today?"}
    ]
)

# Print the assistant's response
print(response['choices'][0]['message']['content'])
