print("Movie Recommendation System project entry point")

from core.movie_manager import MovieManager
from core.user_manager import UserManager
from core.recommender import Recommender

#Create objects
movie_manager = MovieManager()
user_manager = UserManager()

print(user_manager.get_user_ratings(1))


#Create recommender
recommender = Recommender(movie_manager, user_manager)

#Choose a user
user_id = 1

#Get recommendations
recs = recommender.recommend_movies(user_id)

#Display the results
print("\nRECOMMENDATIONS (UNSEEN MOVIES):")
for movie in recs:
    print(movie["title"], "-", movie["genre"])

print("\nALL MOVIES:", movie_manager.get_all_movies())
print("SEARCH TITLE:", movie_manager.search_by_title("batman"))
print("FILTER GENRE:", movie_manager.filter_by_genre("Action"))
print("MIN RATING:", movie_manager.filter_by_rating(8))
print("BY YEAR:", movie_manager.filter_by_year(2010))

movie_manager.close_connection()

