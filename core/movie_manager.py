import sqlite3

class MovieManager:

    def __init__(self, db_name = "database.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_all_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        return self.cursor.fetchall()

    def search_by_title(self, title):
        query = "SELECT * FROM movies WHERE LOWER(Movie_Title) LIKE LOWER(?)"
        self.cursor.execute(query, ('%' + title + '%',))
        return self.cursor.fetchall()

    def filter_by_genre(self, genre):
        query = "SELECT * FROM movies WHERE LOWER(Genre) LIKE LOWER(?)"
        self.cursor.execute(query, ('%' + genre + '%',))
        return self.cursor.fetchall()

    def filter_by_rating(self, min_rating):
        query = "SELECT * FROM movies WHERE IMDB_Rating >= ?"
        self.cursor.execute(query, (min_rating,))
        return self.cursor.fetchall()

    def filter_by_year(self, year):
        query = "SELECT * FROM movies WHERE Release_Year >= ?"
        self.cursor.execute(query, (year,))
        return self.cursor.fetchall()

    def debug_table_structure(self):
        print("Running debug...")
        self.cursor.execute("PRAGMA table_info(movies)")
        print(self.cursor.fetchall())

    def close_connection(self):
        self.conn.close()
