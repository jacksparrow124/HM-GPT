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

class TextToSpeech:
    playExe=""
    def __init__(self) -> None:
        pass
  
    def processText(self,myText):
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text=myText, lang='en', slow=False)
        # Saving the converted audio in a mp3 file named
        # # welcome 
        myobj.save("welcome.mp3")
        # Playing the converted file
        mixer.init()
        mixer.music.load("welcome.mp3")
        mixer.music.play()
        while mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)
        mixer.music.unload
        mixer.quit
        os.remove("welcome.mp3")
        

  

  
