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
prompt = "suggest a name for my food company onluy one word ans give"
message_system = {
    "role":"system",
    "content":"you are a brand manager who suggest name for my food company . name should be in one word."
}
message = {
    "role":role,
    "content":prompt 
}
messages = [message_system, message]
response = client.chat.completions.create(model=model, messages=messages,temperature=2)
print(response.choices[0].message.content)
