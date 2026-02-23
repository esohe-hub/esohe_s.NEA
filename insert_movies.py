import sqlite3
from PreSavedMovies import movies
conn = sqlite3.connect('MovieRecommendationSystem.db')
cursor = conn.cursor()

cursor.executemany('''
    INSERT INTO Movies (Title, Duration, Genre, Director, Actors, Classification, Metascore, Release_Year, ConciseSummary)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', movies)


conn.commit()
conn.close()
