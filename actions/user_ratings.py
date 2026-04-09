from actions.UserAuthentication import user_manager
from core.user_manager import UserManager
user_manager = UserManager()


def rate_movie_ui(user_id):
    movie_id = input("Enter movie ID: ").strip()
    rating = input("Enter rating (0 - 10): ").strip()

    if not rating.isdigit():
        print("Rating must be a number.")
        return

    rating = int(rating)

    if rating < 0 or rating > 10:
        print("Rating myst be between 0 and 10.")
        return

    success = user_manager.rate_movie(user_id, movie_id, rating)

    if success:
        print("Rating saved!")
    else:
        print("Error saving rating.")


'''def rate_movies(user_id):

    print("Enter movies you have enjoyed.")
    print("Type 'done' when you are finished.")

    while True:
        movie_title = input("Movie Title:").strip().title()
        if len(movie_title) == 0:
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
                INSERT INTO User_Ratings (UserID, Rating, Movie_Title, Genre)
                VALUES (?, ?, ?, ?)
            ''', (user_id, rating, MovieTitle, genre)
            )
            print("Movie saved! \n")
        except sqlite3.IntegrityError:
            print("You have already rated this movie.")
        
    conn.commit()
    conn.close()'''
