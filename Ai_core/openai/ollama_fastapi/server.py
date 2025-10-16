from typing import Union
from fastapi import FastAPI, Body, Query, Path, Depends
from ollama import Client

app = FastAPI()
client = Client(
    host = 'http://localhost:11434'
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


def chat(
        message: str = Body(..., description = "The message ")
):
    response = client.chat(model="gemma:2b",messages=[
        {"role":'user','content':message}
    ])
    return {"responce": response.message.content}