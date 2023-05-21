import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY2")

#def speechToText(mp3):
    #input = audio_file("path/to/file/audio.mp3")
    #put the folder you want to save the file to in the .mp3 above
    #audio_file = open(input)
    #transcript = openai.Audio.transcribe("whisper-1", audio_file)

#commenting out open function block that was causing compile errors. Uncomment when there is code to put in here
#def textToSpeech(text):
       #text to speech using whisper library 

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
    print(response["choices"][0]["message"]["content"]) # type: ignore
    










        
