#########################################################################################################

# Delays the display time of each character 
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("hello world\n")

#########################################################################################################

# prints cprint line highlighted red 
from termcolor import cprint
cprint("Hello, World!", "green", "on_red")

#########################################################################################################

#plays specified sound once line is ran
from playsound import playsound
playsound("INSERT_FILENAME_HERE.mp3")

