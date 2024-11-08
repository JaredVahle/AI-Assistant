import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get API details from the environment variables
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

# Function to make a request to the API
def get_api_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    data = {
        "prompt": prompt,
        "max_tokens": 50,
    }
    
    # Send the request
    response = requests.post(API_URL, headers=headers, json=data)
    
    # Check for a successful response
    if response.status_code == 200:
        result = response.json()
        return result.get("choices", [{}])[0].get("text", "No response found")
    else:
        # Handle errors
        return f"Error: {response.status_code}, {response.text}"

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a prompt: ")
    response = get_api_response(user_input)
    print("API Response:", response)
