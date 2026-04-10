class Recommender:
    def __init__(self, movie_manager, user_manager):
        self.movie_manager = movie_manager
        self.user_manager = user_manager

    def get_highly_rated_movies(self, user_id):
        ratings = self.user_manager.get_user_ratings(user_id)
        high_rated = []