# Here's a basic example that simply moves the mouse 5 pixels to the right (relative to its current position):

# import pyautogui

# pyautogui.moveRel(5, 0)

############################################################################################################################################################################################################

# A more interesting example could be a mouse-mover that keeps the computer awake:

import pyautogui
import time
import random

# move = range(100,100)


# while True:
#     print("moving now!")
#     pyautogui.moveRel(100, 0)
#     pyautogui.moveRel(-100, 0)
#     time.sleep(0)

############################################################################################################################################################################################################

# The following Python program will automatically input keypresses to control the Outlook Web App. I don't recommend running it directly, rather, you can modify the example to your own needs.

import pyautogui
import time



# def forwardAndMoveSelectedEmailInOutlookWebApp(addressToSendTo, folderToMoveTo):
#     ## 'Forward' 
#     pyautogui.hotkey('ctrl', 'shift', 'f')
#     time.sleep(4)

#     ## 'To' is active. Type address.
#     pyautogui.write(addressToSendTo, interval=0.05)
#     time.sleep(2)

#     ## Press Enter to pick the address
#     pyautogui.press('enter')
#     time.sleep(1)

#     ## Move the cursor to the body so that we can send
#     pyautogui.press('tab')
#     time.sleep(0.1)
#     pyautogui.press('tab')
#     time.sleep(0.1)
#     pyautogui.press('tab')
#     time.sleep(1)

#     ## 'Send' shortcut
#     pyautogui.hotkey('ctrl', 'enter')
#     time.sleep(4)

#     ## 'Move to folder'
#     pyautogui.press('v')
#     time.sleep(2)

#     pyautogui.write(folderToMoveTo, interval=0.05)
#     time.sleep(1)
#     pyautogui.press('enter')
#     time.sleep(5)


# print("""
# NOTES:
# - SORT OLDEST FIRST!
# - HAVE THE FIRST EMAIL SELECTED!
# - Consider disabling "thread" or "conversation" view -- try both ways and see which you prefer.
# """)
# saidSomething = input("Continue? (y|N)...").lower()
# if saidSomething != "y":
#     import sys
#     sys.exit()
    
# delay = 10
# print()
# print(f"Giving you {delay} seconds to open the window before starting.")
# print("If you aren't ready, Ctrl+C to exit now.")
# for i in range(delay, 0, -1):
#     print(i)
#     time.sleep(1)

# ## You can loop this if you want
# ## for count in range(3):
# forwardAndMoveSelectedEmailInOutlookWebApp("jdoe@example.com", "folderToMoveTo")
