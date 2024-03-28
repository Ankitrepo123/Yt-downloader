from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('700x300')
root.resizable(0, 0)
root.title("YouTube Video Downloader")

Label(root, text='Putt the youtube video link👇',
      font='arial 17 bold',fg="Black").pack()
 
# enter link
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold',fg="Blue").place(x=270, y=60)
Entry(root, width=80, textvariable=link,bd=3).place(x=32, y=90)

# function to download video


def Downloader():

    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=270, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='white',
       padx=2, command=Downloader).place(x=280, y=150)

root.mainloop()