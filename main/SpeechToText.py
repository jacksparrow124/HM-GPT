# used this for reference: https://www.analyticsvidhya.com/blog/2021/12/guide-for-speech-recognition/
import speech_recognition as sr

class SpeechToText:

    recognizer=None

    def __init__(self) -> None:
        pass
    
    def processSpeech(self):
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 50
        recognizer.pause_threshold=3
        print(sr.Microphone.list_microphone_names())
        print(sr.Microphone.list_working_microphones())
        with sr.Microphone(device_index=0) as source:

            recognizer.adjust_for_ambient_noise(source,duration=1)
            print("Start Talking")
            audio_text = recognizer.listen(source,timeout=5,phrase_time_limit=5)
            print("Time over, thank you")
            #print(audio_text)
            try:
                # using google speech recognition
                text=recognizer.recognize_google(audio_text)
                print("Text: "+text)
                return text
            except Exception as e:
                print(e)
                print("Sorry, I did not get that")