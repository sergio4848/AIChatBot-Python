import random
import re

import datasets as datasets
import requests

def get_response(user_input):
    responses = []
    # Search the web for a response
    url = "https://api.openai.com/v1/engines/davinci/completions"
    params = {
        "prompt": user_input,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    response = requests.post(url, json=params).json()
    if "choices" in response:
        responses.append(response["choices"][0]["text"])
    else:
        responses.extend(list(datasets.load_dataset("chatterbot-corpus").map(lambda x: x["text"])))
    return random.choice(responses)

def main():
    print("Welcome to my chatbot!")
    while True:
        user_input = input("What can I help you with today? ")
        print(get_response(user_input))

if __name__ == "__main__":
    main()
