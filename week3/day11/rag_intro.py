import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
knowledge_base = {
    "age":"kalyan's age is 20 years",
    "income":"kalyan's income is 1000000"
}
def retrieve_info(question):
    if "age" in question:
        return knowledge_base["age"]
    elif "income" in question:
        return knowledge_base["income"]
    else:
        return None
    
def ask_llm(question):
    context = retrieve_info(question)
    system_prompt = f"""Answer in one line only and answer based on this context only do not hallucinate context:{context}"""
    system_message = {
        "role":"system",
        "content":system_prompt
    }
    message = {
        "role":"user",
        "content":question
    }
    messages = [system_message, message]
    response = client.chat.completions.create(model=model, messages = messages)
    answer = response.choices[0].message.content
    return answer
question = "what is kalyan income"
print(ask_llm(question))    
