import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("Your openai key 🙂 requires paid account")








#def speechToText(mp3):
 #   input = audio_file("path/to/file/audio.mp3")
  #  audio_file = open(input)
   # transcript = openai.Audio.transcribe("whisper-1", audio_file)

#def textToSpeech(text):
    


def chat(input): 
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",

    messages=[{"role": "user", "content": input}]

    messages=[{"role": "user", "content": "%i"}%input]

    )
    print(completion)

chat("what is the capital of france?")











    