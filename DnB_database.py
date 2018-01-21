import sqlite3
import sys


# Database will contain information about artist, song title and yt link to given song.
# And return information when asked by rest service
class DatabaseOperations:

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



if __name__ == '__main__':

    db = DatabaseOperations()





