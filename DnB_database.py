import sqlite3
import sys

# Database will contain information about artist, song title and yt link to given song.
# And return information when asked by rest service

def create_database(database_file):   # Creating database

    conn = sqlite3.connect(database_file)
    c = conn.cursor()
    try:
        c.execute('CREATE TABLE Dnb_songs(ID INTEGER PRIMARY KEY AUTOINCREMENT, Artist TEXT, Title TEXT);')
        conn.commit()
    except:
        print('Database exist, skipping creation')
    return conn

def add_song(conn,track):

    #sql = ()
    cur = conn.cursor()
    cur.execute("INSERT INTO Dnb_songs VALUES (?,?,?)",track)
    conn.commit()
    return print("Song Added: ", track)

def main():
    audio = [None,"Audio","Genesis Device"]
    db_conn = create_database('dnb.db')
    add_song(db_conn,audio)
    db_conn.close()



main()

