# used this for reference: https://www.analyticsvidhya.com/blog/2021/12/guide-for-speech-recognition/
#for some reason - it doesn't hear my voice on a mac. I will try it on windows when I get back and keep trying on mac during my trip. 
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
recognizer.energy_threshold = 50
recognizer.pause_threshold=3
print(sr.Microphone.list_microphone_names())
print(sr.Microphone.list_working_microphones())

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone(device_index=0) as source:
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Start Talking")
    audio_text = recognizer.listen(source,timeout=5,phrase_time_limit=10)
    print("Time over, thank you")
    #print(audio_text)
    try:
        # using google speech recognition
        print("Text: "+recognizer.recognize_google(audio_text))
    except Exception as e:
         print(e)
         print("Sorry, I did not get that")