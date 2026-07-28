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
def generate_response(prompt):
    message = {
        "role":"user",
        "content":prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

bad_prompt = """This is user complaint: 
my laptop is not working 
classify this
"""

good_prompt="""
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of three categories namely billing, technical, return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word shoud be one of the categories given in constraints
#Example
For instance if a user compalin says he wants a refund then the category is Return
#FALLBACK
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
My laptop is not working
"""
generate_response(bad_prompt)
generate_response(good_prompt)
print(generate_response(bad_prompt))
print(generate_response(good_prompt))