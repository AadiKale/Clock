from tkinter import *
import time
import winsound


def countdown():
    start = int(h.get()) * 3600 + int(m.get()) * 60 + int(s.get())
    while start > -1:
        minute, second = (start // 60, start % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        s.set(second)
        m.set(minute)
        h.set(hour)
        root.update()
        time.sleep(1)
        if start == 0:
            s.set(00)
            m.set(00)
            h.set(00)
        start -= 1
    winsound.PlaySound('Echoing-Timer.wav', winsound.SND_ALIAS)


def click(event):
    countdown()


root = Tk()
root.geometry("300x300+600+300")
root.configure(bg="CadetBlue1")
root.title("Timer")
root.iconbitmap("timer.ico")

Label(root, text="Hr     Min     Sec", font=("Baskerville Old Face", 18), bg="CadetBlue1").place(x=65, y=50)

h = IntVar()
m = IntVar()
s = IntVar()

hr = Entry(root, textvariable=h, font=("Camibria Math", 13), width=8, bg="LightSteelBlue1", bd=3, relief=GROOVE)
hr.place(x=45, y=90)
h.set(00)

mins = Entry(root, textvariable=m, font=("Camibria Math", 13), width=8, bg='LightSteelBlue1', bd=3, relief=GROOVE)
mins.place(x=110, y=90)
m.set(00)

sec = Entry(root, textvariable=s, font=("Camibria Math", 13), width=8, bg='LightSteelBlue1', bd=3, relief=GROOVE)
sec.place(x=180, y=90)
s.set(00)
sec.focus_set()

Button(root, text='SET', font=("Bodoni MT", 14), width=8, bg='LightSteelBlue1', activebackground="LightSteelBlue4",
       activeforeground='snow', relief=RAISED, command=countdown).place(x=95, y=140)
root.bind('<Return>', click)

root.mainloop()
