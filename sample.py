from tkinter import *
mw = Tk()
def say_hello():
    name = userinput.get()
    greeting ='Hello' + name+ '!'
    if name !='':
      text.config (text = 'greeting')
      userinput.delete(0, END)
userinput = Entry(mw,width=20) ,font('Arial', 18)
userinput.pack(padx= 10, pady= 10)
text ='label'(mw,text= 'Enter your Name!'),font('Arial', 14)
text.pack(pady=5)
btn = Button(mw, text='say Hello!'),font ('Arial',12, command ="sayHello")
btn.pack(pady=20)

mw.mainloop()