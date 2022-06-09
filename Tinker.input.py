from tkinter import *
# create  mainwindow
mw = Tk()

def clicked():
    mylabel = Label(mw,text = "Python program"), font ('Arial', 12)
    mylabel.pack(pady = 10)

# creating input
user_input= Entry(mw)
user_input.pack(pady=10)

# creating buttons
my_button = Button(mw,text='Click Me!',padx = 20,pady = 10,font('Arial',14),command= clicked)
my_button.pack(padx=50 , pady=30)

mw.mainloop()
