from flask import Flask
import sqlite3
import sys

#Rest service will get information from client and using parameters will extract record from database

class Db_Operations:

    def __init__(self):

        self.database = 'dnb.db'
        self.db_conn = self.create_database()
        self.cur = self.db_conn.cursor()

    def create_database(self):  # Creating or connecting to database

        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        try:
            c.execute(
                'CREATE TABLE Dnb_songs(Id INTEGER PRIMARY KEY AUTOINCREMENT, Artist TEXT, Title TEXT, YT_Link TEXT);')
            conn.commit()
        except:
            print('Database exist, skipping creation', sys.exc_info()[0])
        print('Database connected')
        return conn

    def add_song(self, track):  # Adds track in format Artist | Song | link

        self.cur.execute("INSERT INTO Dnb_songs(Artist,Title,YT_Link) VALUES (?,?,?)", track)
        self.db_conn.commit()
        return print("Song Added: ", track)

    def get_all(self):
        all = self.cur.execute("SELECT * from Dnb_songs")
        return all

    def get_all_links(self):
        response = self.cur.execute("SELECT YT_link from Dnb_songs")
        decoded = response.fetchall()
        return decoded


# Flask part and routing:
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to DnB Jukebox REST - commands : /all for all songs" \
           "/links - for youtube links"

@app.route('/all')
def return_all():
    all = ""
    records = db.get_all()
    alllist = records.fetchall()
    for a in alllist:
        all += " "+str(a)
    return all


@app.route('/links')
def give_links():
    yt_links_list = db.get_all_links()
    return str(yt_links_list)




if __name__ == '__main__':
    db = Db_Operations()
    app.run()
