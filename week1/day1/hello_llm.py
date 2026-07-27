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
prompt = "who is ms dhoni"
message = {
    "role":role,
    "content":prompt 
}
messages = [message]
response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)
