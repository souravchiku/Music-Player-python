from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
#Harrington'
global ResumeButton,PlayButton,PauseButton

#Defining buttons important functions
def musicurl():
    dd=filedialog.askopenfilename()
    print(dd)
    audiotrack.set(dd)
def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    audiostatuslabel.configure(text='Playing.......')
    
def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    audiostatuslabel.configure(text="Paused")
def volumnup():
    vol=mixer.music.get_volume()
    if (vol>=vol*100):

        mixer.music.set_volume(vol+0.1)
    else:
        mixer.music.set_volume(vol+0.1)

def volumndown():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
def stopmusic():
    mixer.music.stop()
    audiostatuslabel.configure(text="Stopped")

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    audiostatuslabel.configure(text="Playing......")

#Ceating Widthes
def widthes():

    global imbrowse,implay,imstop,impause,imvolumnup,imvolumndown,imresume
    global audiostatuslabel
    #images register
    imbrowse=PhotoImage(file='search.png')
    implay=PhotoImage(file='play.png')
    imstop=PhotoImage(file='stop.png')
    imvolumnup=PhotoImage(file='up.png')
    impause=PhotoImage(file='pause.png')
    imvolumndown=PhotoImage(file='down.png')
    imresume=PhotoImage(file='play.png')
    #change size of image
    imbrowse=imbrowse.subsample(6,6)
    implay=implay.subsample(6,6)
    imvolumnup=imvolumnup.subsample(6,6)
    imvolumndown=imvolumndown.subsample(6,6)
    imstop=imstop.subsample(3,4)
    impause=impause.subsample(6,6)
    imresume=imresume.subsample(6,6)
    #labels
    trackLabel=Label(root,text='Select From Track:',bg='dark slate gray',font=('Harrington',20,'italic bold'),fg='ghost white',)
    trackLabel.grid(row=0,column=0,padx=30,pady=30)

    #audiostatus label
    audiostatuslabel=Label(root,text='',bg='dark slate gray',font=('Harrington',20,'italic bold'),fg='ghost white')
    audiostatuslabel.grid(row=1,column=1)
    #entry box
    trackLabelEntry=Entry(root,font=('Harrington',15,'italic bold'),width=35,textvariable=audiotrack)
    trackLabelEntry.grid(row=0,column=1)
    #buttons
    BrowseButton = Button(root,text='Search',font=('chiller',15,'italic bold'),width=100,bd=3,image=imbrowse,compound=LEFT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=30,pady=30)

    StartButton = Button(root,text='Play',font=('chiller',15,'italic bold'),width=115,bd=3,image=implay,compound=RIGHT,command=playmusic,activebackground='black')
    StartButton.grid(row=1,column=0,padx=30,pady=30)

    root.PauseButton = Button(root,text='Pause',font=('chiller',15,'italic bold'),width=115,bd=5,image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=3,column=0,padx=30,pady=30)

    root.ResumeButton = Button(root,text='Resume',font=('chiller',15,'italic bold'),width=115,bd=5,image=imresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=3,column=0,padx=30,pady=30)
    root.ResumeButton.grid_remove()



    VolumnUpButton = Button(root,text='volumn Up',font=('chiller',15,'italic bold'),width=115,bd=3,image=imvolumnup,compound=RIGHT,command=volumnup)
    VolumnUpButton.grid(row=1,column=2,padx=30,pady=30)

    StopButton = Button(root,text='Stop',font=('chiller',15,'italic bold'),width=80,bd=3,image=imstop,compound=CENTER,command=stopmusic)
    StopButton.grid(row=2,column=1,padx=30,pady=30)

    VolumnDownButton = Button(root,text='volumn Down',font=('chiller',15,'italic bold'),width=115,bd=3,image=imvolumndown,compound=RIGHT,command=volumndown)
    VolumnDownButton.grid(row=3,column=2,padx=30,pady=30)
    #Progress label
    ProgressBarLabel=Label(root,text='',bg='black')
    ProgressBarLabel.grid(row=1,column=2,rowspan=4)
    ProgressBarVolume=Progressbar(ProgressBarLabel,orient=VERTICAL,mode='determinate',value=20,length=190)
    ProgressBarVolume.grid(row=0,column=0,ipadx=5)
    
    ProgressbarVolumeLabel=Label(ProgressBarLabel,text='0%',bg='lightgray')
    ProgressbarVolumeLabel.grid(row=0,column=0)

     


root=Tk()
root.title("Music Player")
root.iconbitmap("icon.ico")
root.geometry("1000x540+200+100")
root.configure(bg='dark slate gray')
#global variables
audiotrack=StringVar()
mixer.init()
widthes()



root.mainloop()