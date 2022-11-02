from Basic import speak
from getCommands import takeMic
import wikipedia

def Wikipedia():
    speak("What would you like to search for?")
    search = takeMic()
    speak("Searching on wikipedia")
    result = wikipedia.summary(search, sentences = 2)
    print(result)
    speak(result)
    
    