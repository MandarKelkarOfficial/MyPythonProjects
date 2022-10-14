from tkinter import *
from tkinter import filedialog
from pytube import YouTube
#from moviepy import *
#from moviepy.editor import  VideoFileClip
import shutil

def  select_path():
    path=filedialog.askdirectory()
    p1.config(text=path)

'''def download_file():
    #get user path
    get_link=e1.get()
    #get selected path
    user_path=p1.cget("text")
    screen.title("Downloading..........")

    #download video
    vid=YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip=VideoFileClip(vid)
    vid_clip.close()

    #moving file to selected folder
    shutil.move(vid,user_path)
    screen.title("Download complete!.......") '''
screen=Tk()
screen.title("Youtube Download")
can=Canvas(screen,width=500,height=500)
can.pack()

#adding image
img=PhotoImage(file='yt.png')
#resize
img=img.subsample(2,2)
can.create_image(250,80,image=img)

#getting labels
e1=Entry(screen,width=40,font="arial 15")
l1=Label(screen,text="Enter Download Link:",font="arial 15")

#adding entry and label to canvas
can.create_window(250,170,window=l1)
can.create_window(250,220,window=e1)


#select path label and buttons
p1=Label(screen,text="Select Path for Download",font="arial 15")
sel_btn=Button(screen,text="Select Path",bg="red",padx='22',pady='5',font="arial 15",fg='#fff',command=select_path)
#d_btn=Button(screen,text="Download",bg="green",padx='22',pady='5',font="arial 15",fg='#fff',command=download_file)

#adding widgets to window
can.create_window(250,280,window=p1)
can.create_window(250,330,window=sel_btn)
#can.create_window(250,390,window=d_btn)




screen.mainloop()