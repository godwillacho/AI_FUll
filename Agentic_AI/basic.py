from urllib import response
from httpx import request
from pydantic import BaseModel 
from openai import OpenAI 
from dotenv import load_dotenv
import  requests as request

load = load_dotenv()
client = OpenAI()

def weather_getter(city : str):
     url =  f'//wtty.in/{city.lower()}?format=%C+%t'
     response = request.get(url)
     
     if response.status_code == 200:
          return f' The weather in {city} is {response.text}'
     
     return ' Could Not get the weather data for {city} at the moment '


def main():
    user_query = input('Ask anyquestion :')
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': "user",
             "content": user_query}
        ]
    )
    print(f"🤖: {response.choices[0].message.content}")

main()
