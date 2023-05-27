import os
from dotenv import load_dotenv
import openai
import time
import smtplib
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText
import countio
#import tiktoken

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY2")


def chat(input): 
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": input}]
    )
    return completion

#begin main loop
print("welcome. My name is burt. i will be helping you today... 😈")
while True:
    question=input(">>>")
    response=chat(question)
   # print(response) (for debugging)
    print(response["choices"][0]["message"]["content"]) #type: ignore

