from tkinter import *
from urllib import request
import webbrowser
import random


# Class for song library operations :


class Track_Operations:
    # Starting parameters -  (local host for now)
    def __init__(self):
        self.url = "http://127.0.0.1:5000/"


    def get_yt_links(self): # Method to get youtube link of song, returns list of youtube links
        r = request.urlopen(self.url + "links")
        links_in_string = r.read().decode("utf-8")
        return links_in_string.split(',),')

    def prep_link(self,link): # Deletes abundant characters from link preparing right format for webbrowser
        return link[3:-1]

    def open_in_browser(self,link): # Opens provided link
        webbrowser.open(link)

    def get_random_link(self,yt_links_list):

        ran_number = random.randint(0, len(yt_links_list))
        random_link = yt_links_list[ran_number]
        preped_link = self.prep_link(random_link)
        return preped_link

    def play_random_song(self):

        all_links = self.get_yt_links()
        ran_link = self.get_random_link(all_links)
        self.open_in_browser(ran_link)

    def get_track_list(self):

        r = request.urlopen(self.url + "all")
        all_decoded = r.read().decode("utf-8")
        return print(all_decoded)


class Gui:

    def __init__(self,master):
        self.track_op = Track_Operations()
        self.master = master
        master.title("DnB jukebox")

        self.photo = PhotoImage(file='dnb.gif')
        self.bg_label = Label(master, image=self.photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.dnb_jukebox_label = Label(master, text="Long live Drum and Bass", bg="green")
        self.dnb_jukebox_label.place(x=135)

        self.play_button = Button(master, text="Play!", command=self.track_op.play_random_song, bg="red")
        self.play_button.place(x=50, y=75, anchor=N)

        self.info_button = Button(master,text ="info", command=self.info_window)
        self.info_button.place(x=350, y=200)

        self.tl_button = Button(master, text="Track list", command=self.track_list)
        self.tl_button.place(x=50,y=111, anchor=N)



    def info_window(self):

        self.top = Toplevel(height=200,width=400,bg ="red")
        self.top.title("Info")
        self.top.geometry()


    def track_list(self):

        self.tl_window = Toplevel()
        self.tl_window.title("Track list")


        self.get_button = Button(self.tl_window, text="GET", command=self.track_op.get_track_list)
        self.get_button.pack()

        self.tl_label = Label(text=self.track_op.get_track_list)
        self.tl_label.pack()


if __name__ == '__main__':

    root = Tk()
    root.geometry("400x224")
    dnb_jukebox = Gui(root)
    root.mainloop()

