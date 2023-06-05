# Se usó esto como referencia: https://www.analyticsvidhya.com/blog/2021/12/guide-for-speech-recognition/
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
            print("Empieza a hablar")
            audio_text = recognizer.listen(source,timeout=5,phrase_time_limit=5)
            print("Tiempo más, gracias.")
            #print(audio_text)
            try:
                # Uso del reconocimiento de voz de Google
                text=recognizer.recognize_google(audio_text)
                print("Text: "+text)
                return text
            except Exception as e:
                print(e)
                print("Lo siento, no entendí eso")