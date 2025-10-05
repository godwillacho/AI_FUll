from openai import  OpenAI
from  dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key = 'AIzaSyABO2mgElYUv1Ytd6O4BneOZCtoNsHCSkk',
    base_url = 'https://generativelanguage.googleapis.com/v1beta/'
)
system = """
 'You are a medical specialist.Make sure you answer only to Queries in the medical field. You are a medical specialist.Make sure you answer only to Queries in the medical field.'
 Output Format:
{{
'code':"string" or null,
"isCodingQuestion":boolean
}}

 Examples:
 Q: Ebola 
 A: This is a deseace outbreak that occured in africa a very deadly deesease that killed hundreds of people provide.
 provide its syntoms and known remedies 
"""
responce = client.chat.completions.create(
    model='gemini-2.5-flash',
    messages = [
        {'role':'system' , 'content' : system},
        {"role": 'user',"content":'Ebola'}
    ]
)

print(responce.choices[0].message.content)