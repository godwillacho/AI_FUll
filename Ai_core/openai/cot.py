from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

# Loading google gemini api key into the chat gpt library
client = OpenAI(
    api_key = 'AIzaSyABO2mgElYUv1Ytd6O4BneOZCtoNsHCSkk',
    base_url = 'https://generativelanguage.googleapis.com/v1beta/'
)

SYSTEM_PROMPT = """
        YOure an expert AI Assistant in resolving user euwries using chain of thought.
        you work on START, PLAN and OUTPUT steps.
        You need to first PLAN what needs to be done.The PLAN can be multiple steps.
        ONce you think enough PLAN has been done, finally you can give an OUTPUT.

        Rules:
        -Strictly follow the given JSON output format
        -ONly run one step at a time .
        -The sequence of steps is START( where user gives an input),PLAN (That can be multiple times ) and finally OUTPUT (which is going to be displayed to the user ).

        Output JSON Format:
        {"step":"START" | "PLAN" | "OUTPUT" , "content": " string" }

        EXMPLE 
        START: Hey, can you solve 2+ 3* 5 / 10 
        PLAN:{"step": "PLAN": "content": "Seems like the user is interested in maths problem "}
        PLAN:{"step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method"}
        PLAN:{"step": "PLAN": "content": "Yes, The BODMAS is  right way to solve this equation"}
        PLAN:{"step": "PLAN": "content": "first we must multiply 3 * 5 which is 15"}
        PLAN:{"step": "PLAN": "content": "Now the new equation is 2+ 15 /10"}
        PLAN:{"step": "PLAN": "content": "we must perform devide that is 15/10 = 1.5"}
        PLAN:{"step": "PLAN": "content": "Now the new equation is 2+ 1.5 "}
        PLAN:{"step": "PLAN": "content": "finally we add 2 +1.5 = 3.5 "}
        PLAN:{"step": "PLAN": "content": "Great, We have solved and finally left with 3.5 as ans"}
        OUTPUT:{"step":"PLAN": "content": "3.5"}
        
        
        

"""

responce = client.chat.completions.create(
    model = 'gemini-2.5-flash',
    response_format = {'type': 'json_object'},
    messages = [
        {'role':'system' , 'content' : SYSTEM_PROMPT},
        {"role": 'user' , "content":'hey write a code to add n numbers in javascript '},
        {"role" : 'assistant' ,  "content": json.dumps( {"step": "PLAN" , "content": "You want a JavaScript code to add 'n' numbers."} ) },
        {"role" : 'assistant' ,  "content": json.dumps({"step": "PLAN", "content": "The user wants JavaScript code to add 'n' numbers."}) },
        {"role" : 'assistant' ,  "content": json.dumps( {"step": "PLAN", "content": "I will create a JavaScript function that accepts 'n' numbers using rest parameters."} ) },
        {"role" : 'assistant' ,  "content": json.dumps( {"step": "PLAN", "content": "I will then use the `reduce` method to sum all the numbers efficiently."} ) }
    ]
)

print(responce.choices[0].message.content)