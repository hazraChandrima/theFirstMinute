# Script to automatically open WhatsApp for those stupid birthday wishes to someone, we all know it's a pain in the butt to stay awake, be it your bestie's bday or anyone you don't care about
# This script can also be modified to text anything to anyone, like sending hundreds of wholesome good morning GIFs to friends and family
# This is meant for the desktop version of WhatsApp(Windows only). For the web browser version, use web_script.py
import pyautogui
import time

# Adjust accordingly
CONTACT_NAME = "Tuli"
MESSAGE = f"Wish you a very Happy Birthday dear {CONTACT_NAME}!!"

# used as reference for calculation of screen coordinates for different screen sizes
BASE_HEIGHT=1080
BASE_WIDTH=1920

# Scales the coordinates according to screen size of your device
def scale_xy(x,y):
    current_width, current_height = pyautogui.size()
    scaled_x = int(x * (current_width / BASE_WIDTH))
    scaled_y = int(y * (current_height / BASE_HEIGHT))
    return scaled_x, scaled_y


def send_message():

    # Opens WhatsApp (only for Windows systems)
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.typewrite('WhatsApp')
    pyautogui.press('enter')
    time.sleep(2)

    # Searching for the contact, then opening it and typing the message, it's that fucking easy!
    # You don't need to adjust any coordinates, the calculations take care of it
    searchbar_x, searchbar_y = scale_xy(150, 120) # coordinates for search bar
    contact_x, contact_y = scale_xy(200, 250)  # coordinates for first topmost name that appears after searching

    # clicks on search bar to search for contact
    pyautogui.click(x=searchbar_x, y=searchbar_y)
    time.sleep(1)
    pyautogui.typewrite(CONTACT_NAME) # searches for contact name
    time.sleep(2)

    # clicks on first search result after searching
    pyautogui.click(x=contact_x, y=contact_y)
    time.sleep(2)

    # writes the message in text box
    pyautogui.typewrite(MESSAGE)
    time.sleep(1)

    pyautogui.press('enter') # finally, sends the message


send_message()



