# this is the simplified version see original speechToText.py for more detailed attempt
# used this for reference: https://www.analyticsvidhya.com/blog/2021/12/guide-for-speech-recognition/
#for some reason - it doesn't hear my voice on a mac. I will try it on windows when I get back and keep trying on mac during my trip. 

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Go ahead!")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Understood: %s" % text)
    except:
        print("Couldnt recognize your voice")