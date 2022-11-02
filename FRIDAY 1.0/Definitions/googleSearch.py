import webbrowser as web
from Basic import speak
from getCommands import takeMic

def googleSearch():
    speak("What would you like to search for?")
    search = takeMic()
    web.open('https://www.google.com/search?q='+search)
    
    if search != "null":
            web.open('https://www.google.com/search?q='+search)
    else:
        speak("Would you like to try searching on Google again?")

