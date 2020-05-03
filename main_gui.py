#req, pillow for image, pip install pillow 
# import tkinter
from tkinter import *
# import menu module
from tkinter import Menu
from tkinter import filedialog
# import webbrowser module
import webbrowser
# import logo module
from PIL import Image
from PIL import ImageTk

#set variables
url = 'http://github.com/thattkyle/py_parity'
#open website for user help
def openwebsite():
    webbrowser.open_new(url)
    
#button click
def sourceclicked():
    folder_src = sourcelbl.configure(filedialog.askdirectory())
    print(folder_src)
def destclicked():
    folder_dst = destlbl.configure(filedialog.askdirectory())
    

#set main.window
window = Tk()
#set window.size
window.geometry("750x300")
#set window.title
window.title("pyParity")

#create menu
menu = Menu(window)
menu.help = Menu(menu, tearoff=0)
menu.help.add_command(label="Help", command = openwebsite)
menu.help.add_command(label="Quit", command = menu.quit)
menu.add_cascade(label='File', menu=menu.help)

#add buttons
#source
sourcelbl = Label(window, text="Please select source folder")
sourcelbl.grid(column=0,row=0)
sourcebtn = Button(window, text="Select", command = sourceclicked)
sourcebtn.grid(column=1, row=0)
#destination
destlbl = Label(window, text="Please select destination folder")
destlbl.grid(column=0,row=1)
destbtn = Button(window, text="Select", command = destclicked)
destbtn.grid(column=1, row=1)


#add filedialog
#srcfolder = filedialog.askdirectory()

window.config(menu=menu)
window.mainloop()