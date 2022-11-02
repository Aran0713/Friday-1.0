import pyautogui
import webbrowser as web
from time import sleep

def sendWhatsappMsg(phone_no, message):
    Message = message
    web.open('http://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(5)
    pyautogui.press('enter')
    sleep(5)
    
username = {
    'myself': '+1 647 619 0713',
    'brother': '+1 647 482 4246',
    'dad': '+1 416 418 0037',
    'mom': '+1 647 779 8572',
    'poo': '+1 647 608 7633',
    'kish': '+1 647 332 2215',
    'meera': '+1 416 655 2240',
    'zip': '+1 416 824 0567',
    'mark': '+1 647 533 1234',
    'box': '+1 647 632 1709'
}
