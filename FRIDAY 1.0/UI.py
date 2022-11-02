from cProfile import label
from tkinter import *
import os
from turtle import width
import pyautogui
os.system('cls')
import datetime

width, height = pyautogui.size()

def GUI():
    ##### Top Left corner #####
    dateWidth = str(round(0.08*width))
    dateHeight = str(round(0.08*width))
    year = str(datetime.datetime.now().year)
    day = str(datetime.datetime.now().day)
    monthNum = datetime.datetime.now().month
    month = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

    # date = Tk()
    date.title('')
    date.geometry(dateWidth+"x"+dateHeight+"+5+5")
    date.configure(bg="black")
    # Month label
    monthLabel = Label(date, text=month[monthNum], bg="black", fg="white", font=("Courier, 30"))
    monthLabel.pack()
    # Day label
    dayLabel = Label(date, text=day, bg="black", fg="white", font=("Courier, 30"))
    dayLabel.pack()



    ##### Top Right #####
    voiceWidth = str(round(0.30*width))
    voiceHeight = str(round(0.13*width))
    voiceXPosition = str(round(width-int(voiceWidth)-20))

    # voice = Tk()
    voice.title('')
    voice.geometry(voiceWidth+"x"+voiceHeight+"+"+voiceXPosition+"+20")
    voice.configure(bg="black")
    # Voice labels
    voiceLabel1 = Label(voice, text="Goodnight", bg="black", fg="blue", font=("Courier, 13"), wraplength=550, justify="center").pack(pady=10)
    voiceLabel2 = Label(voice, text="The date is July 21st 2022", bg="black", fg="white", font=("Courier, 13"), wraplength=550, justify="center").pack(pady=10)
    voiceLabel3 = Label(voice, text="Hey Friday what's the date today", bg="black", fg="blue", font=("Courier, 13"), wraplength=550, justify="center").pack(pady=10)
    voiceLabel4 = Label(voice, text="Friday is now at your service", bg="black", fg="white", font=("Courier, 13"), wraplength=550, justify="center").pack(pady=10)




    ##### Top  Center #####
    fridayWidth = str(round(0.4*width))
    fridayHeight = str(round(0.2*height))
    fridayXPosition = str(round(0.22*width))

    # friday = Tk()
    friday.title('')
    friday.geometry(fridayWidth+"x"+fridayHeight+"+"+fridayXPosition+"+15")
    friday.configure(bg="black")
    # Friday label
    monthLabel = Label(friday, text="F.R.I.D.A.Y", bg="black", fg="white", font=("Courier, 45"))
    monthLabel.pack()



    ##### Bottom Left #####
    stockWidth = str(round(0.18*width))
    stockHeight = str(round(0.55*height))
    stockYPosition = str(round(0.30*height))

    # stock = Tk()
    stock.title('')
    stock.geometry(stockWidth+"x"+stockHeight+"+20+"+stockYPosition)
    stock.configure(bg="black")
    # Stock label
    stockLabel = Label(stock, text="Stocks", bg="black", fg="white", font=("Courier 10 underline"), )
    stockLabel.pack(pady=5, anchor="w")


    ##### Bottom Right #####

    toDoWidth = str(round(0.18*width))
    toDoHeight = str(round(0.5*height))
    toDoXPosition = str(round(width-int(toDoWidth)-20))
    toDoYPosition = str(round(0.35*height))

    # toDo = Tk()
    toDo.title('')
    toDo.geometry(toDoWidth+"x"+toDoHeight+"+"+toDoXPosition+"+"+toDoYPosition)
    toDo.configure(bg="black")
    # todo label
    toDoLabel = Label(toDo, text="To Do List", bg="black", fg="white", font=("Courier 20 underline"))
    toDoLabel.pack(pady=10)
    # list 
    progress = [
        "Finish Friday app", "Connect to microcomputer", "Microphone and external speaker", "Computer vision", "Ultron"
    ]
    for i in progress:
        listNum = Label(toDo, text="- "+ i, bg="black", fg="white", font=("Courier 10"),  wraplength=330)
        listNum.pack(padx= 5, pady=5, anchor="w")
        

    ##### Bottom center #####
    matterWidth = str(round(0.55*width))
    matterHeight = str(round(0.53*height))
    matterXPosition = str(round(0.22*width))
    matterYPosition = str(round(0.35*height))

    # matter = Tk()
    matter.title('')
    matter.geometry(matterWidth+"x"+matterHeight+"+"+matterXPosition+"+"+matterYPosition)
    matter.configure(bg="black")
    # Matter At Hand label
    matterLabel = Label(matter, text="Matter At Hand", bg="black", fg="white", font=("Courier 10 underline"), )
    matterLabel.pack(pady=5, anchor="w")

    """
    matter.mainloop()
    toDo.mainloop()
    stock.mainloop()
    date.mainloop()
    friday.mainloop()
    voice.mainloop()
    
    """
