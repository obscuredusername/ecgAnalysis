import os
import requests
import google.generativeai as genai

# Replace with your environment variable name
API_KEY = os.environ.get("AIzaSyAmyL5DDKnIEmamkf6NcoBW-lI0PIRaPQg")

# Set the model name (e.g., "gemini-pro")
model_name = "gemini-pro"

# Define your prompt here
prompt = "Write a poem about a cat."

# Set the request headers with your API key
headers = {"Authorization": f"Bearer {API_KEY}"}

# Prepare the request data with the prompt
data = {"contents": [{"parts": [{"text": prompt}]}]}

# Send the POST request to the API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={API_KEY}"
response = requests.post(url, headers=headers, json=data)

# Check for successful response
if response.status_code == 200:
  # Parse the response JSON
  response_json = response.json()
  # Access the generated text
  generated_text = response_json["contents"][0]["generatedText"][0]
  print(f"Generated Text: {generated_text}")
else:
  print(f"Error: {response.status_code}")
