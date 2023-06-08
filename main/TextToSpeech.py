#Text to Speech sample code
#https://www.geeksforgeeks.org/convert-text-speech-python/

# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
import pygame
from pygame import mixer  # Load the popular external library
import time

counter=1
class TextToSpeech:
    playExe=""
  
    def __init__(self) -> None:
        pass
  
    def processText(self,myText):
        global counter
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text=myText, lang='en', slow=False)
        # Saving the converted audio in a mp3 file named
        # # welcome 
        file_name = "welcome"+ str(counter)+ ".mp3"
        myobj.save(file_name)
        # Playing the converted file
        mixer.init()
        mixer.music.load(file_name)
        mixer.music.play()
        while mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
        mixer.music.unload
        mixer.quit
        counter = counter + 1
        if counter == 10:
            counter = 1

    