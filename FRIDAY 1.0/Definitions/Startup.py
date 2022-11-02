import datetime
from Basic import speak
 
 
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir")
    else:
        speak("For you sir, I'm always up")
        
def startup():
    greeting()
    #date()
    #time()
    speak("Friday is now at your service")
    
    