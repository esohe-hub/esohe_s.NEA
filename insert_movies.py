from database_connection import get_connection
from PreSavedMovies import movies

def insert_connection():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT OR IGNORE INTO Movies (Title, Duration, Genre, Director, Actors, Classification, Metascore, Release_Year, ConciseSummary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', movies)


    conn.commit()
    conn.close()
