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