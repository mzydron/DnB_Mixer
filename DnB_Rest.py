from flask import Flask
from Dnb_Mixer import DnB_database

#Rest service will get information from client and using parameters will extract record from database


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to DnB Mixer"

@app.route('/artist')
def return_artist():
    artist = ""
    db = DnB_database.Database()
    art = db.get_artist()
    artlist = art.fetchall()
    for a in artlist:
        artist += " "+str(a)

    return artist








if __name__ == '__main__':
    app.run()
