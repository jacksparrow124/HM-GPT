import os
from dotenv import load_dotenv
import openai
import time


import SpeechToText as st
import TextToSpeech as ts


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY2")



def chat(input): 
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": input}]
    )
    return completion

#begin main loop
print("bienvenido. Mi nombre es burt. Te estaré ayudando hoy... 😈")
speechToText=st.SpeechToText()
textToSpeech=ts.TextToSpeech()
while True:
    question=speechToText.processSpeech()
    response=chat(question)
    #print(response) #(for debugging)
    content=response["choices"][0]["message"]["content"]
    #content ="this is a test"
    print(content) #type: ignore
    textToSpeech.processText(content)

