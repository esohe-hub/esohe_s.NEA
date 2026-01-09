import sqlite3

def rate_movies(user_id):
    conn = sqlite3.connect('MovieRecommendationSystem.db')
    cursor = conn.cursor()

    print("Enter movies you have enjoyed.")
    print("Type 'done' when you are finished.")

    while True:
        movie_title = input("Movie Title:").strip().title()
        if type(movie_title) != str:
            print("Invalid title. Please enter a valid movie title.")
        if len(movie_title) == 0:
            print("Movie title cannot be empty.")
        if movie_title.lower() == 'done':
            break

        while True:    
            try:
                rating = float(input(f"Rating for '{movie_title}' (0 - 10) :"))
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
            genre = input(f"Genre of '{movie_title}': ").strip().title()
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
        ''', (user_id, rating, movie_title, genre)
        )
        print("Movie saved! \n")
    except sqlite3.IntegrityError:
        print("You have already rated this movie.")
        
    conn.commit()
    conn.close()


#getting user inputs to store in the database for our recommendations
#Parameterised queries are used to prevent SQL injection attacks by seperating SQL code from data which improves security.
