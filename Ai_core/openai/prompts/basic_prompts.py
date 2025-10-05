from openai import  OpenAI
from  dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key = 'AIzaSyABO2mgElYUv1Ytd6O4BneOZCtoNsHCSkk',
    base_url = 'https://generativelanguage.googleapis.com/v1beta/'
)

responce = client.chat.completions.create(
    model='gemini-2.5-flash',
    messages = [
        {'role':'system' , 'content' : 'You are a medical specialist.Make sure you answer only to Queries in the medical field.If it is impossible to link query to medicine field tell them you dont know.make the answers to be bullet point and well sumarised for easy reading'},
        {"role": 'user', "content" : 'Her syntompts are a painful neck and her head feels heavy'}
    ]
)

print(responce.choices[0].message.content)