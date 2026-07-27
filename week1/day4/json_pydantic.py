import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
myapi_key = os.getenv("GROQ_API_KEY")
if not myapi_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
client = Groq(api_key=myapi_key)
model = "llama-3.3-70b-versatile"
role = "user"


from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    phone_number: str
    location: str
schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}    
system_prompt = f""" Extract the personal information from the ticket strictly based on this schema and give a json output.{schema}"""
message_system = {
    "role": "system",
    "content": system_prompt
}
text = 'MY name is John and I am a software engineer. I love coding and exploring new technologies.MY EMAIL IS abc@gmail.com i live in hyderabad i have iphone which is not working my mobile number is 888979432'
prompt = f"Extract the name,email, phone number, and location from the following text: {text}"
message = {
    "role":role,
    "content":prompt 
}
messages = [message_system,message]
response = client.chat.completions.create(model=model, messages=messages,response_format=response_format)
answer = response.choices[0].message.content
print(answer)

import json
raw_json = answer
datafile = json.loads(raw_json)
ticket = Ticket(**datafile)
print(ticket.name)
print(ticket.email)
print(ticket.phone_number)
print(ticket.location)

