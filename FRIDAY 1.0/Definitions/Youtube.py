import pywhatkit
from Basic import speak
from getCommands import takeMic

def youtube():
    speak("What would you like to search for on youtube?")
    topic = takeMic()
    if topic != "null":
        pywhatkit.playonyt(topic)
    else:
        speak("Would you like to try playing something on Youtube again?")