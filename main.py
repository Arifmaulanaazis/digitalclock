from tkinter import *
import time

def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)


root  = Tk()
root.title("Jam Digital")
root.geometry("450x200")
root.resizable(0,0)
root.iconbitmap("icon.ico")
clock=Label(root,font=("times",50,"bold"))
clock.grid(row=1,column=0,pady=25,padx=100)
times()

digi = Label(root,text="Jam Digital",font="times 24 bold")
digi.grid(row=0,column=0)
nota=Label(root,text="Jam      Menit      Detik", font="times 15 bold")
nota.grid(row=3,column=0)
root.attributes('-topmost',True)
root.mainloop()
