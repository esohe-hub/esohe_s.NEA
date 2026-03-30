import sqlite3
from DatabaseConnection import get_connection


def rate_movies(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    print("Enter movies you have enjoyed.")
    print("Type 'done' when you are finished.")

    while True:
        MovieTitle = input("Movie Title:").strip().title()
        if len(MovieTitle) == 0:
            print("Movie title cannot be empty.")
            continue
        if MovieTitle.lower() == 'done':
            break

        while True:    
            try:
                rating = float(input(f"Rating for '{MovieTitle}' (0 - 10) :"))
                if 0 <= rating <= 10:
                    break
                else:
                    print("The rating must be between 0 and 10.")
            except ValueError:
                print("Invalid rating.")
                continue

        while True:
            allowed_genres = [
                "Action",
                "Comedy",
                "Romance",
                "Horror",
                "Sci-Fi",
                "Drama",
                "Thriller",
                "Fantasy"
            ]
            print("Available genres:", ",".join(allowed_genres))
            genre = input(f"Genre of '{MovieTitle}': ").strip().title()
            if genre not in allowed_genres:
                print("Invalid genre. Please choose from the mentioned genres.")
                continue
            if len(genre) == 0:
                print("Genre cannot be empty.")
            else:
                genre = genre.title()
                break
        try:
            cursor.execute('''
                INSERT INTO Ratings (UserId, Rating, Movie_title, Genre)
                VALUES (?, ?, ?, ?)
            ''', (user_id, rating, MovieTitle, genre)
            )
            print("Movie saved! \n")
        except sqlite3.IntegrityError:
            print("You have already rated this movie.")
        
    conn.commit()
    conn.close()


