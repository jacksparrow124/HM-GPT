import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("your openai key")

#def speechToText(mp3):
#   input = audio_file("path/to/file/audio.mp3")
#  audio_file = open(input)
# transcript = openai.Audio.transcribe("whisper-1", audio_file)

#def textToSpeech(text):
        

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
    print(response["choices"][0]["message"]["content"])
    










        
