from openai import OpenAI
import os
from dotenv import load_dotenv
import time as t

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        if char == '.' or char == '?' or char == '!':
            t.sleep(2.5)

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
    print(" ")
    print("="*50)

def gaveQuestion(question):
    student_response = input(question)
    # relevant API documenation: https://platform.openai.com/docs/guides/text-generation
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "developer",
                "content": ("You are a retired professional poker AI player named AnteAI."
                            "You are now teaching a student about poker."
                            "You keep your responses concise and to the point."
                            "You will ask the student a question about a topic of poker."
                            "When they respond, let them know if their answer is acceptable. If their answer is not"
                            "Acceptable, give them some feedback on how they may improve.")
            },
            {
                "role": "assistant",
                "content": question
            },
            {
                "role": "user",
                "content": student_response
            }
        ]
    )

    slow_print(completion.choices[0].message.content)
    print(" ")
    print("="*50)