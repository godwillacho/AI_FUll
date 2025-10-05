from openai import  OpenAI
from  dotenv import load_dotenv

import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
        You are and AI assistant nameed Acho.
        You are acting on behalf of Acho who is 25 years old Tech Ethusiatic and IT technical Support .
        Your main tech stack is python and c# and you are learning generative AI These days.

        Examples:
        Q. Hey
        A. Hey, Whatss up !

        (100 -150 examples)

"""
response = client.chat.completions.create(
    model='gpt-4o',
    messages = [
        {'role':'system' , 'content' : SYSTEM_PROMPT},
        {"role": 'user',"content":'who are you '}
    ]
)
print("Response:",response.choices[0].message.content)