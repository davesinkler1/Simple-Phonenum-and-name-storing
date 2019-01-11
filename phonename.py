#This is a software for storing names and phone numbers
#The output will be stored in a file

import tkinter


window = tkinter.Tk()
Mainmenu = tkinter.Menu(window)
window.config(menu = Mainmenu)
MenuFile = tkinter.Menu(Mainmenu, tearoff = 0)
Mainmenu.add_cascade(label = "File", menu = MenuFile)
MenuFile.add_command(label = "Exit", command = window.destroy)



window.title("Phone-o-data")
window.geometry("800x600")

NameInfo = tkinter.Label(window, text="Name:")
NameInfo.pack()

NameEntry = tkinter.Entry(window, width = 70)
NameEntry.pack()

NumberInfo = tkinter.Label(window, text="Phone Number:")
NumberInfo.pack()

NumberEntry = tkinter.Entry(window, width = 70)
NumberEntry.pack()

def read_write():
  file = open("datatext.txt", "w")
  file.write(NameEntry.get() + '\n')
  file.write(NumberEntry.get() + '\n')
  
SubmitText = tkinter.Label(window, text = "Submit the data")
SubmitText.pack()

SubmitButton = tkinter.Button(window, text = "Submit", command = read_write)
SubmitButton.pack()

window.mainloop()