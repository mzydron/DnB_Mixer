
from urllib import request
import webbrowser
import random

# Client will be responsible for sending orders using put method to rest api. In return it will get link to the youtube
# site which later will be played on youtube

# Class for song library operations (Add/Update/Remove:
class Track_Operations:
    # Starting paramets - for now local host
    def __init__(self):
        self.url = "http://127.0.0.1:5000/"


    def get_yt_links(self): # Method to get youtube link of song, returns
        r = request.urlopen(self.url + "links")
        links_in_string = r.read().decode("utf-8")
        return links_in_string.split(',),')



    def prep_link(self,link): # Deletes abundant characters from link
        return link[3:-1]

    def open_in_browser(self,link):
        webbrowser.open(link)



    def get_random_link(self,yt_links_list):

        ran_number = random.randint(0,len(yt_links_list))
        random_link = yt_links_list[ran_number]
        preped_link = self.prep_link(random_link)
        return preped_link





def play_random_song():
    operator = Track_Operations()
    all_links = operator.get_yt_links()
    ran_link = operator.get_random_link(all_links)
    operator.open_in_browser(ran_link)




