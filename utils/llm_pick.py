from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

def pick_llm(level: str):
    if level.lower() == "low":
        llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)
    elif level.lower() == "medium":
        llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
    elif level.lower() == "high":
        llm = ChatGroq(model="qwen/qwen3.6-27b", temperature=0)
    else:
        raise ValueError(f"Unsupported level: {level}")
    return llm


llm_obj = pick_llm("low")  
print(llm_obj.invoke("What is the capital of France?"))