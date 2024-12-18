# This is meant for the desktop version of WhatsApp for Windows only.
import time
import pyautogui

# Adjust accordingly, can also be modified for texting anything else
CONTACT_NAME = "Tuli"
MESSAGE = f"Wish you a very Happy Birthday dear {CONTACT_NAME}!!"

# used as reference for calculation of screen coordinates for different screen sizes
BASE_HEIGHT=1080
BASE_WIDTH=1920

# scales the coordinates according to screen size of your device
# you don't need to adjust any coordinates, the calculations take care of it
def scale_xy(x,y):
    current_width, current_height = pyautogui.size()
    scaled_x = int(x * (current_width / BASE_WIDTH))
    scaled_y = int(y * (current_height / BASE_HEIGHT))
    return scaled_x, scaled_y


def send_message():

    # Opens WhatsApp
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.typewrite('WhatsApp')
    pyautogui.press('enter')
    time.sleep(2)

    searchbar_x, searchbar_y = scale_xy(150, 120) # coordinates for search bar
    contact_x, contact_y = scale_xy(200, 250)  # coordinates for first topmost contact that appears after searching

    # clicks on search bar to search for the contact
    pyautogui.click(x=searchbar_x, y=searchbar_y)
    time.sleep(1)
    pyautogui.typewrite(CONTACT_NAME) # searches for contact name
    time.sleep(2)

    # clicks on first search result
    pyautogui.click(x=contact_x, y=contact_y)
    time.sleep(2)

    # writes the message in text box
    pyautogui.typewrite(MESSAGE)
    time.sleep(1)

    pyautogui.press('enter') # sends the message
    time.sleep(1)

    pyautogui.hotkey('alt', 'f4') # finally, closes WhatsApp


if __name__ == "__main__":
    send_message()



