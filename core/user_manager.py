import sqlite3
from DatabaseConnection import get_connection

class UserManager:

    def get_user_movies(self, user_id):
        self.cursor.execute('''SELECT Movies.* FROM Movies JOIN User_Ratings ON Movies.MovieId = User_Ratings.MovieId WHERE User_Ratings.UserId = ? ''', (user_id,))
        return self.cursor.fetchall()

    def get_user_ratings(self, user_id):
        self.cursor.execute("SELECT * FROM user_ratings WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def create_user(self, username, password):
        try:
            self.cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True # user created successfully
        except sqlite3.IntegrityError:
            return False #username already exists

    def get_user_by_username(self, username):
        self.cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def rate_movie(self, user_id, movie_id, rating):
        try:
            self.cursor.execute("INSERT INTO User_Ratings (UserId, MovieId, Rating) VALUES (?,?,?)", (user_id, movie_id, rating))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
