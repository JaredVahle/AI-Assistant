import openai
import env  # Importing from env as specified

# Set your API key from the env module
openai.api_key = env.API_KEY

# Function to send a prompt and get a response using gpt-4o-mini
def ask_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Using gpt-4o-mini as specified
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

# Example usage to get a response
prompt = "How can I improve my code efficiency?"
answer = ask_openai(prompt)
print(answer)

# Optional: List available models
models = openai.Model.list()
print("Available Models:")
for model in models['data']:
    print(model['id'])
