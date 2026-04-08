import sqlite3

class MovieManager:

    def __init__(self, db_name = r"C:\Users\user\Downloads\newfolder\esohe_s.NEA\data\MovieRecDatabase.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()


    def get_all_movies(self):
        self.cursor.execute("SELECT * FROM Movies")
        return self.cursor.fetchall()

    def search_by_title(self, title):
        query = "SELECT * FROM Movies WHERE LOWER(Movie_Title) LIKE LOWER(?)"
        self.cursor.execute(query, ('%' + title + '%',))
        return self.cursor.fetchall()

    def filter_by_genre(self, genre):
        query = "SELECT * FROM Movies WHERE LOWER(Genre) LIKE LOWER(?)"
        self.cursor.execute(query, ('%' + genre + '%',))
        return self.cursor.fetchall()

    def filter_by_rating(self, min_rating):
        query = "SELECT * FROM Movies WHERE IMDB_Rating >= ?"
        self.cursor.execute(query, (min_rating,))
        return self.cursor.fetchall()

    def filter_by_year(self, year):
        query = "SELECT * FROM Movies WHERE Release_Year >= ?"
        self.cursor.execute( query, (year,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
