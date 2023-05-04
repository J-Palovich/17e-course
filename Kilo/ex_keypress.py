## Inspired by https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
from tkinter import *

wn = Tk()
wn.geometry("700x350")


# Define a function to display the message
def key_press(e):
   label.config(text="Welcome to TutorialsPoint")

def key_released(e):
   label.config(text="Press any Key...")
# Create a label widget to add some text
label = Label(wn, text= "", font= ('Helvetica 17 bold'))
label.pack(pady= 50)

# Bind the Mouse button event
wn.bind('<KeyPress>',key_press)
wn.bind('<KeyRelease>',key_released )
wn.mainloop()

# def down(e):
#     print('Down\n', e.char, '\n', e)

# def up(e):
#     print('Up\n', e.char, '\n', e)

# wn.bind('<KeyPress>', down)
# wn.bind('<KeyRelease>', up)

# wn.mainloop()