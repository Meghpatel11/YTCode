from tkinter import *
from speedtest import Speedtest

root = Tk()
root.title("Internet Speed Checker")
root.geometry('400x400')
root.resizable(False,False)

bg_image = PhotoImage(file='speed.png')
bg = Label(image=bg_image).grid(row=0,column=0,padx=100,pady=5)

def get_speed():
    s = Speedtest()
    download = s.download()
    upload = s.upload()
    download_speed = round(download/(10**6),2)
    upload_speed = round(upload/(10**6),2)
    down_lab.config(text='Download Speed is: ' + str(download_speed) + "Mbps")
    upload_lab.config(text='Upload Speed is: ' + str(upload_speed) + "Mbps")

fg = '#0cc6a9'
bg = '#ed4947'

Button(root,text='Get Speed',font=('Arial',10,'bold'),command=get_speed,bg=bg).grid(row=1,column=0,padx=5,pady=10)

down_lab = Label(root,text='',fg=fg,font=('Helvetica',10,'bold'))
down_lab.grid(row=2,column=0,pady=5,padx=5)

upload_lab = Label(root,text='',fg=fg,font=('Helvetica',10,'bold'))
upload_lab.grid(row=3,column=0,pady=5,padx=5)

root.mainloop() 

