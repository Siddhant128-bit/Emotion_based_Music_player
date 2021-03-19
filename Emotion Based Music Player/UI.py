from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
import os

window=Tk()
window.title('EMUSIC')
window.geometry('1050x320')
window.configure(background='White')
icon_image=PhotoImage(file='UI data/logo.png')

frame0=LabelFrame(window)
frame0.configure(bg='white')

def Play():
    os.system('python video.py')
    window.update()
    os.chdir('././')
def info():
    os.system('Information.txt')



window.iconphoto(False,icon_image)
Label(window,text='',background='white').grid(row=0,column=0)
icon_play=PhotoImage(file='UI data/Play.gif')
Button(window,text='Play Music',image=icon_play,width=200,height=200,command=Play).grid(row=10,column=20)

img=ImageTk.PhotoImage(Image.open('UI Data/Main.gif'))
img_Label=Label(image=img)
img_Label.grid(row=10,column=40)

icon_play1=PhotoImage(file='UI data/Aboutus.gif')
Button(window,text='Play Music',image=icon_play1,width=200,height=200,command=info).grid(row=10,column=50)


window.mainloop()
