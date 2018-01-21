from tkinter import *
from Dnb_Mixer import DnB_Client


class Gui:

    def __init__(self,master):

        self.master = master
        master.title("DnB jukebox")

        self.photo = PhotoImage(file='dnb2.gif')
        self.bg_label = Label(master, image=self.photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.dnb_jukebox_button = Button(master, text="DnB jukebox")
        self.dnb_jukebox_button.place(x=50,y=50, anchor=CENTER)

        self.play_button = Button(master, text="Play!", command =DnB_Client.play_song)
        self.play_button.place(x=50, y=75, anchor=N)




if __name__ == '__main__':

    root = Tk()
    root.geometry("400x224")
    dnb_jukebox = Gui(root)
    root.mainloop()

