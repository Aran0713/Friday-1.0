import speech_recognition as sr #pip install SpeechRecognition
from Basic import speak


def takeCMD():
    query = input()
    return query

def takeMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-CA")
        print(query)
    except Exception as e:
        print(e)
        # speak("Sorry I didn't get that")
        return "null"
    return query