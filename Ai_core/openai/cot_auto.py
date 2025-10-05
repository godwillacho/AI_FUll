from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

# Loading google gemini api key into the chat gpt library
client = OpenAI(
    # api_key = 'AIzaSyABO2mgElYUv1Ytd6O4BneOZCtoNsHCSkk',
    # base_url = 'https://generativelanguage.googleapis.com/v1beta/'
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


message_history =[
    {"role": "system" , "content" :SYSTEM_PROMPT},
    ]
user_query = input("Enter your querry ")
message_history.append({"role" : "user" , "content": user_query})
print('/n/n/n/n/n/n/n')

while True:
    responce = client.chat.completions.create(
        model = 'gpt-4o',
        response_format = {'type': 'json_object'},
        messages=message_history 
    )
    raw_result = responce.choices[0].message.content
    message_history.append({"role" : "user" , "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get('step') == 'START':
        print(f'Starting /n  {parsed_result.get('content')}')
        continue

    if parsed_result.get('step') == 'PLAN':
        print(f'Starting /n  {parsed_result.get('content')}')
        continue
    if parsed_result.get('step') == 'OUTPUT':
        print(f'Starting /n  {parsed_result.get('content')}')
        break