from DatabaseConnection import get_connection
from PreSavedMovies import movies

def insert_movies():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT OR IGNORE INTO Movies (Title, Duration, Genre, Director, Actors, Classification, Metascore, Release_Year, ConciseSummary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', movies)


    conn.commit()
    conn.close()
insert_movies()