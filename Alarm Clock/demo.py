from tkinter.ttk import *
from tkinter import *

from datetime import datetime
from time import sleep

from pygame import mixer

#window
window = Tk()
window.title("")
window.geometry('350x150')

def sound_alarm():
    mixer.music.load('alarmtune.mp3')
    mixer.music.play()
    
def alarm():
    while True:
        control = 1
        print(control)
        
        alarm_hour ='03'
        alarm_minute ='12'
        alarm_sec ='00'
        alarm_period ='AM'.upper()
        
        now = datetime.now()
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")
        
        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec ==second:
                            print("Time to take a break")
                            sound_alarm()
        sleep(1) 
                          
            
    
mixer.init()
alarm()

window.mainloop()

