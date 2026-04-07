import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def complete_prompt(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_input = input("Enter a prompt: ")
    completion = complete_prompt(user_input)
    print("Completion:", completion)