import pyautogui
import time

CONTACT_NAME = "Tuli"
MESSAGE = "hi!"

def send_message():

    #Opens WhatsApp
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.typewrite('WhatsApp')
    pyautogui.press('enter')
    time.sleep(2)

    #Searching for the contact, then opening it and typing the message, it's that fucking easy!
    pyautogui.click(x=150, y=120)
    time.sleep(1)
    pyautogui.typewrite(CONTACT_NAME)
    time.sleep(2)
    pyautogui.click(x=200, y=250)
    time.sleep(1)
    pyautogui.typewrite(MESSAGE)
    time.sleep(1)
    pyautogui.press('enter')


send_message()


