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
    print(response["choices"][0]["message"]["content"]) #type: ignore

#while time(2628000):
   # openai.tokens(tiktoken) #counts how many tokens used in 30 days
#
#mailserver = smtplib.SMTP('smtp.gmail.com',)
#msg = MIMEMultipart()
#msg['From'] = ['gpt232323@gmail.com']
#msg['To'] = ['your email adress']
#msg['Subject'] = ['Your Monthly Token Usage And questions asked 🙂']
#message = ('Your monthly spending of tokens is: %i'% openai.tokens(tiktoken))
#msg.attach(MIMEText(message))









        
