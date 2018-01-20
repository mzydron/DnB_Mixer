from urllib import request
from urllib import request
import webbrowser

# Client will be responsible for sending orders using put method to rest api. In return it will get link to the youtube
# site which later will be played on youtube

#Class for song library operations (Add/Update/Remove:
class Track_Operations():
    # Starting paramets - for now local host
    def __init__(self):
        self.url = "http://127.0.0.1:5000/"


    def get_all(self): # Method to get youtube link of song, returns HTTPResponse object
        r = request.urlopen(self.url + "all")
        return r


    def get_data_list(self,res_object): # Converts response object into text and substracts information in form of list
        info = res_object.read().decode("utf-8")
        listed_data = info.split()
        return listed_data

    def get_link(self,listed_data):
        linker = listed_data[4]
        link = linker[1:-1]
        return link

    def open_in_browser(self,link):
        webbrowser.open(link)

def main():
    operator = Track_Operations()
    all_info = operator.get_all()
    data_list = operator.get_data_list(all_info)
    link = operator.get_link(data_list)
    operator.open_in_browser(link)
    print("Done")


main()