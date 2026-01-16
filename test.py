'''from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="phi3:mini",
    temperature=0.0,
)

response = llm.invoke("hello,say me who you are in short. What is your name? which model are you?")
print(response.content)
'''
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="gemma3:270m",
    temperature=0.0,
)

response = llm.invoke("hello,say me who you are in short")
print(response.content)
