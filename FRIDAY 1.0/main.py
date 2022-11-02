from email import message
import sys
sys.path.insert(0, './Definitions')
from Startup import *
from getCommands import *
from Basic import *
from Whatsapp import *
from googleSearch import *
from wiki import *
from Youtube import *
from weather import *

# from UI import *
# from nltk.tokenize import word_tokenize

if __name__ == "__main__":
    wakeWord = "friday"
    while True:
        #Takes input
        query = takeMic().lower()
        # query = word_tokenize(query)
        if (wakeWord in query):
            startup()
            
            while True:
                query = takeMic().lower()
                # Output the date today
                if 'date' in query:
                    date()
                
                # Outputs the time 
                if 'time' in query:
                    time()
                    
                # Can change voice from male to female 
                male = ["voice", "male"]
                female = ["voice", "female"]
                if all(i in query for i in female):
                    setVoice("female")
                elif all(i in query for i in male):
                    setVoice("male")
                    
                # Sends Whatsapp message to whoever
                typeMessage = ["type", "message"]
                if all(i in query for i in typeMessage):
                    try:
                        speak("To whom do you want to send a message to?")
                        print("Name:")
                        name = takeCMD().lower()
                        if (name == ""): 
                            speak("Would you like to try sending a message again?")
                            continue
                        phone_no = username[name]    
                        print(phone_no)
                        
                        speak("What would you like to send?")
                        print("Message:")
                        message = takeCMD()
                        if (message == ""):
                            speak("Would you like to try sending a message again") 
                            continue
                        
                        sendWhatsappMsg(phone_no, message)
                        speak("The message to " +name+ " has been sent")
                    except Exception as e:
                        speak("Sorry, they are not in my database")
                elif 'message' in query:
                    try:
                        speak("To whom do you want to send a message to?")
                        name = takeMic().lower()
                        if (name == "null"): 
                            speak("Would you like to try sending a message again?")
                            continue
                        phone_no = username[name]    
                        print(phone_no)
                        
                        speak("What would you like to send?")
                        message = takeMic()
                        if (message == "null"):
                            speak("Would you like to try sending a message again") 
                            continue
                        
                        sendWhatsappMsg(phone_no, message)
                        speak("The message to " +name+ " has been sent")
                    except Exception as e:
                        speak("Sorry, they are not in my database")
                        
                # Search 
                if 'wikipedia' in query:
                    Wikipedia()
                elif 'search' in query:
                    googleSearch()
                    
                if 'youtube' in query:
                    youtube()
                
                if 'weather' in query:
                    print(temp)
                    print(description)
                    print(humidity)
                    print(wind_speed)
                    speak("The weather in Toronto is "+ temp +" degrees celsius with a "+ description +". The humidity is "+ humidity +" and the wind speed is "+wind_speed )
                elif 'temperature' in query:
                    print(temp)
                    speak("The temperature in Toronto is "+ temp +" degrees celsius")
                
                
                # Closes Friday/ the whole app
                closeApp = ["close", "stop", "bye", "goodnight", "mute", "go to sleep"]
                if any(i in query for i in closeApp):
                    print("Shutting down")
                    break
                
                

        

# takeMic == "hey jarvis what is the date today" tokenize = ['hey', 'jarvis', 'what', 'is', 'the', 'date', 'today']
