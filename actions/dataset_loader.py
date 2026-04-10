import csv
import sqlite3


conn = sqlite3.connect(r'C:\Users\user\Downloads\newfolder\esohe_s.NEA\database.sqlite')
cursor = conn.cursor()

with open('../data/movie-dataset.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)


    for row in reader:

        movie_title = row['Movie_Title'] if row['Movie_Title'] else None
        release_year = int(row["Release_Year"]) if row["Release_Year"] else None
        classification = row['Classification'] if row['Classification'] else None
        duration = int(row["Duration"].split()[0]) if row["Duration"] else None
        genre = row['Genre'] if row['Genre'] else None
        imdb_rating = float(row["IMDB_Rating"]) if row["IMDB_Rating"] else None
        concise_summary = row['Concise_Summary'] if row['Concise_Summary'] else None
        metascore = int(row["Metascore"]) if row["Metascore"] else None
        director = row['Director'] if row['Director'] else None
        actor1 = row['Actor1'] if row['Actor1'] else None
        actor2 = row['Actor2'] if row['Actor2'] else None
        actor3 = row['Actor3'] if row['Actor3'] else None
        actor4 = row['Actor4'] if row['Actor4'] else None
        num_of_votes = int(row["NumOfVotes"]) if row["NumOfVotes"] else None

        cursor.execute(
           '''
           INSERT OR IGNORE INTO movies
           (Movie_Title, Release_Year, Classification, Duration, Genre, IMDB_Rating, Concise_Summary, Metascore, Director, Actor1, Actor2, Actor3, Actor4, NumOfVotes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
           ''',
            (movie_title, release_year, classification, duration, genre, imdb_rating, concise_summary, metascore, director, actor1, actor2, actor3, actor4, num_of_votes)
        )

conn.commit()
conn.close()

