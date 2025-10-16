from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional
import requests


load = load_dotenv()
client = OpenAI()


class MyOutputFormat(BaseModel):
    step : str = Field (..., description = 'The ID of the step . Example: PLAN, OUTPUT ,TOOL ,INPUT ,OBSERVE')
    content : Optional[str] = Field(None, description = "The optional string content  ")
    tool : Optional[str] = Field(None, description = "The ID of the tool to call.")
    input : Optional[str] = Field (None, description= 'The input parametre for the tool ') 