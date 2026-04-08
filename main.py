print("Movie Recommendation System project entry point")

from core.movie_manager import MovieManager

manager = MovieManager()

print("ALL MOVIES:", manager.get_all_movies())
print("SEARCH TITLE:", manager.search_by_title("batman"))
print("FILTER GENRE:", manager.filter_by_genre("Action"))
print("MIN RATING:", manager.filter_by_rating(8))
print("BY YEAR:", manager.filter_by_year(2010))

manager.close_connection()