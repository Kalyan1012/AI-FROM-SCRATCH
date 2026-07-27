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
prompt1 = "HI!"
prompt2 = "tell me in detail about time travel"
prompt3 = "tell me about machine learning in detail"
prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    messages =[{
        "role":role,
        "content":prompt
    }]
    response = client.chat.completions.create(model=model, messages=messages,max_tokens=50)
    usage = response.usage
    print(f"Prompt: {prompt}")
    print(f"your token usage is: {usage.prompt_tokens}")
    print(f"completion token usage is: {usage.completion_tokens}")
    print(f"total token usage is: {usage.prompt_tokens + usage.completion_tokens}")
    print(f"Finish reason: {response.choices[0].finish_reason}")