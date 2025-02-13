import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()
def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

root = Tk()

textv=StringVar()

obj=LabelFrame(root, text="Text To Speech",front=20, bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

ldl=Label(obj,text="Text",front=30)
ldl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,front=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",front=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)
         
root.title("Text To Speech")
root.geometry("400x200")
root.resizable(False,False)
root.mainloop()
