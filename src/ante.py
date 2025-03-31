# conda env config vars set -n base OPENAI_API_KEY=$OPENAI_API_KEY
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        if char == '.':
            t.sleep(3)

def askQuestion(question):
    # relevant API documenation: https://platform.openai.com/docs/guides/text-generation
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": (f"You are a retired professional poker AI player named AnteAI. You are now teaching a student about poker. You keep your responses concise and to the point. {question}")
            }
        ]
    )
    slow_print(completion.choices[0].message.content)
 
    print("="*50)
