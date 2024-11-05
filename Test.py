
import openai
import env
# Set your API key here


openai.api_key = env.API_KEY

# Function to send a prompt and get a response
def ask_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the model, such as gpt-4
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

# Example usage
prompt = "How can I improve my code efficiency?"
answer = ask_openai(prompt)
print(answer)
