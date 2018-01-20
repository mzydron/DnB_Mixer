import sqlite3
import sys


# Database will contain information about artist, song title and yt link to given song.
# And return information when asked by rest service
class DatabaseOperations:

    def __init__(self):

        self.database = 'dnb.db'
        self.db_conn = self.create_database()
        self.cur = self.db_conn.cursor()



if __name__ == '__main__':

    db = DatabaseOperations()
    all = db.get_all()
    print(all.fetchall())



