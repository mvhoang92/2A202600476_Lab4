import os
from dotenv import load_dotenv
import langchain_openai
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
print(llm.invoke("đồi gió hú là tác phẩm của ai").content)