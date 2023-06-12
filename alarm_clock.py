from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("Wakey Wakey!!")
        winsound.PlaySound('Echoing-Timer.wav', winsound.SND_ALIAS)
        break


def actual_time():
    set_alarm = f"{hour.get()}:{minute.get()}:{sec.get()}"
    alarm(set_alarm)


def click(event):
    alarm();

# window for app
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x300+600+300")
clock.configure(bg="CadetBlue1")
clock.iconbitmap('clock.ico')

# required labels
time_format = Label(clock, text="Enter time in 24 hr format", font=("Candara", 18, 'bold'), bg="CadetBlue1")
time_format.place(x=75, y=250)
set_time = Label(clock, text=" Hr   Min   Sec", font=("Calibri Light", 18), bg="CadetBlue1")
set_time.place(x=160, y=50)
ring = Label(clock, text="Set Alarm", font=("Constantia", 16), bg="CadetBlue1")
ring.place(x=20, y=80)

# variables to set alarm
hour = IntVar()
minute = IntVar()
sec = IntVar()

# Time required to set the alarm clock
hourtime = Entry(clock, textvariable=hour, width=9, bg="LightSteelBlue1", relief=GROOVE)
hourtime.place(x=150, y=90)
hourtime.focus_set()
mintime = Entry(clock, textvariable=minute, width=9, bg="LightSteelBlue1", relief=GROOVE)
mintime.place(x=200, y=90)
hourtime = Entry(clock, textvariable=sec, width=9, bg="LightSteelBlue1", relief=GROOVE)
hourtime.place(x=250, y=90)

# Take alarm time input from user
setTime = Button(clock, text="SET", font=("Cambria", 14), justify='center', width=8, relief=RAISED,
                 bg="LightSteelBlue1", activebackground="LightSteelBlue4", activeforeground="snow")
setTime.place(x=180, y=130)

clock.bind('<Return>', click)

clock.mainloop()
