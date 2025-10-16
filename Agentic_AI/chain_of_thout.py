from openai import OpenAI
from dotenv import load_dotenv
import json
import re
import requests as request

load_dotenv()

# Loading google gemini api key into the chat gpt library
client = OpenAI(
    # api_key = 'AIzaSyABO2mgElYUv1Ytd6O4BneOZCtoNsHCSkk',
    # base_url = 'https://generativelanguage.googleapis.com/v1beta/'
)

def get_weather(city : str):
    # Use a full URL scheme and a more reliable provider (wttr.in)
    if not city:
        return "No city provided"

    url = f'https://wttr.in/{city.lower()}?format=%C+%t'
    try:
        response = request.get(url, timeout=5)
    except Exception as e:
        return f'Could not fetch weather for {city}: {e}'

    if response.status_code == 200:
        return f'The weather in {city} is {response.text.strip()}'

    return f'Could not get the weather data for {city} at the moment (status {response.status_code})'
available_tools = {
    "get_weather" : get_weather
}

SYSTEM_PROMPT = """
        You are an expert AI Assistant in resolving user enquires using chain of thought.
        you work on START, PLAN and OUTPUT steps.
        You need to first PLAN what needs to be done.The PLAN can be m120386ultiple steps.
        Once you think enough PLAN has been done, finally you can give an OUTPUT.
        you can also call a tool if required from the list of available tools 
        for every tool call wait for the observe step which is the output from the callled tool 

        Rules:
        -Strictly follow the given JSON output format
        -ONly run one step at a time .
        -The sequence of steps is START( where user gives an input),PLAN (That can be multiple times ) and finally OUTPUT (which is going to be displayed to the user ).

        Output JSON Format:
        {"step":"START" | "PLAN" | "OUTPUT" | "TOOL" , "content": " string"."tool" : "string", "input": "string" }

        Available Tools:
        - get_weather : Takes city name as an input string and returns the city info about the city 

        Example 1:
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
        
        Example 2:
        START: What is the weather of Dubai healthcare city? 
        PLAN:{"step": "PLAN": "content": "seems like user is interested in getting weather of Dubai "}
        PLAN:{"step": "PLAN": "content": "Lets see if we have any available tools from the list of available tools "}
        PLAN:{"step": "PLAN": "content": "Great , we have get_weather tool available for this query "}
        PLAN:{"step": "PLAN": "content": "I need to call get_weather tool for Dubai as input for the tool  "}
        PLAN:{"step": "TOOL": "tool": "get_weather" "content": "Dubai  "}
        PLAN:{"step": "OBSERVE": "tool": "get_weather" ,"output":I need to call get_weather tool for Dubai as input for the tool  "}
        PLAN:{"step": "PLAN": "content": "I got the current weather conditions in Dubai  "}
        PLAN:{"step": "PLAN": "content": "Great, i got the weather in Dubai and it a cloudy and windy day with temperatures at about 17 celsuis  "}
       

"""


message_history =[
    {"role": "system" , "content" :SYSTEM_PROMPT}
]
user_query = input("Enter your querry ")
message_history.append({"role" : "user" , "content": user_query})
print(f'\n\n\n\n\n\n\n')

while True:
    responce = client.chat.completions.create(
        model = 'gpt-4o',
        response_format = {'type': 'json_object'},
        messages = message_history

    )
    raw_result = responce.choices[0].message.content
    message_history.append({"role" : "user" , "content": raw_result})
    if raw_result is not None:
        parsed_result = json.loads(raw_result)
    else:
        print("Error: No content received from the model.")
        break

    if parsed_result.get('step') == 'START':
        print("Starting\n  ", parsed_result.get('content'))
        continue
    if parsed_result.get('step') == 'TOOL':
        tool_to_call = parsed_result.get('tool')
        tool_input = parsed_result.get('input')
        # If the model forgot to include 'input' in the TOOL step, try to recover it from the content
        if not tool_input:
            content_text = parsed_result.get('content', '') or ''
            # try patterns like "using <city> as input" or "for <city>"
            m = re.search(r"using\s+([A-Za-z\s,]+?)(?:\s+as input|\s*$)", content_text, re.IGNORECASE)
            if not m:
                m = re.search(r"for\s+([A-Za-z\s,]+?)(?:\?|\.|\s|$)", content_text, re.IGNORECASE)
            if m:
                tool_input = m.group(1).strip()

        print('⚒️:', tool_to_call, '(', tool_input, ')')

        if not tool_input:
            print('Tool input missing — asking the model to provide an explicit "input" field in the TOOL JSON.')
            # Ask the model to correct its output
            message_history.append({
                'role': 'user',
                'content': 'Your TOOL step is missing the "input" field. Please re-emit the JSON with both "tool" and "input".'
            })
            continue

        tool_response = available_tools.get(tool_to_call, lambda x: f"Unknown tool: {tool_to_call}")(tool_input)
        print('⚒️:', tool_to_call, '(', tool_input, ') =', tool_response)
        # Correctly store the observation back into the conversation history
        message_history.append({
            'role': 'developer',
            'content': json.dumps({
                "step": "OBSERVE",
                "tool": tool_to_call,
                "input": tool_input,
                "output": tool_response
            })
        })
        continue

    if parsed_result.get('step') == 'PLAN':
        print("Starting\n  ", parsed_result.get('content'))
        continue
    if parsed_result.get('step') == 'OUTPUT':
        print("Starting\n  ", parsed_result.get('content'))
        break