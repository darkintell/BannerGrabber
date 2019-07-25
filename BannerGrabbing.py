
############Author : Mr.Salvatore##########
import urllib.request
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox as mbox
from socket import *
win = Tk()
win.geometry("450x550")
win.title("Grabber")
win.resizable(0,0)

lAuthor = Label(win,text = "Author :Mr.Salvetore")
lsub = Label(win,text ="Subscribe to : https://t.me/BambooTech")


lip = Label(win,text ="")

scrol= scrolledtext.ScrolledText(win,width = 60,height = 30)


n= StringVar()
entry1 = Entry(win,width =29,textvariable = n)


def sscan():
    site = n.get()
    scrol.delete('1.0', END)
    try:
        server = urllib.request.urlopen("https://"+site)
        for key, value in server.headers.items():
            scrol.insert(INSERT,key+":"+value+"\n")
        lip.configure(text ="Site IP :"+gethostbyname(site))
    except:
        mbox.showerror("Error","Enter A Valid Url!!")

bscan= Button(win,text ="Scan",command = sscan)

lexample = Label(win,text = "Enter Site url (ex : google.com):")

lAuthor.grid()
lsub.grid()
lexample.grid(columnspan =2,rowspan=2,sticky=W)
entry1.grid(sticky =E,row =2)
lip.grid()
scrol.grid()
bscan.grid()

win.mainloop()
