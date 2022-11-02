import datetime
import pyttsx3 # text to speech library

engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 173)  

### Speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

### To get the date (Month/Day/Year)
def date():
    year = str(datetime.datetime.now().year)
    monthNum = datetime.datetime.now().month
    day = str(datetime.datetime.now().day)
    
    month = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

    print("The current date is, " + month[monthNum] +", "+ day +", "+ year)
    speak("The current date is, " + month[monthNum] +", "+ day +", "+ year)
    
### To get the time (Hour/Min/Sec)
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #hours:mins:secs
    print("The current time is "+ Time)
    speak("The current time is "+ Time)
    
### To change voices (male, female) 
def setVoice(voice):
    voices = engine.getProperty('voices')
    
    if voice == "male":
        engine.setProperty('voice', voices[0].id)
        print("You have now switched the voice to male")
        speak("You have now switched the voice to male")
    elif voice == "female":
        engine.setProperty('voice', voices[1].id)
        print("You have now switched the voice to female")
        speak("You have now switched the voice to female")
    
    
