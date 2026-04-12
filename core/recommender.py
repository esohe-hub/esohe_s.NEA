class Recommender:

    def __init__(self, movie_manager, user_manager):
        self.movie_manager = movie_manager
        self.user_manager = user_manager

    def get_highly_rated_movies(self, user_id):
        ratings = self.user_manager.get_user_ratings(user_id)

        high_rated = []
        for row in ratings:
            if row[2] >= 3:
                high_rated.append(row)

        return high_rated


    def get_preferred_genres(self, high_rated):
        genres = []

        for row in high_rated:
            genres.append(row[4])

        return list(set(genres))

    def find_similar_movies(self, genres):
        all_movies = self.movie_manager.get_all_movies()

        filtered = []

        for movie in all_movies:
            movie_genres = movie[5].lower().split(",")

            for genre in genres:
                for mg in movie_genres:
                    if genre.lower() in movie[5].lower():
                        filtered.append({
                            "id": movie[0],
                            "title": movie[1],
                            "genre": movie[5],
                            "rating": movie[6]
                    })
                    break #only break when match is found
                else:
                    continue
                break

        print("USER GENRES:", genres)
        print("SAMPLE MOVIE GENRE:", all_movies[0][5])
        return filtered

    def remove_seen_movies(self, movies, seen_movies):

        seen_titles = set()

        for movie in seen_movies:
           seen_titles.add(movie[3])

        filtered = []

        for movie in movies:
            if movie["title"] not in seen_titles:
                filtered.append(movie)

        return filtered

    def recommend_movies(self, user_id):
        high_rated = self.get_highly_rated_movies(user_id)
        print("HIGH RATED:", high_rated)

        genres = self.get_preferred_genres(high_rated)
        print("GENRES:", genres)


        similar_movies = self.find_similar_movies(genres)
        print("SIMILAR MOVIES:", similar_movies)

        recommendations = self.remove_seen_movies(similar_movies, high_rated)
        print("FINAL RECOMMENDATIONS:", recommendations)

    def get_recommendations(self, user_id, limit=10):

        #get user data
        high_rated = self.get_highly_rated_movies(user_id)
        preferred_genres = self.get_preferred_genres(high_rated)

        all_rated = self.user_manager.get_user_ratings(user_id)

        movies = self.movie_manager.get_all_movies()

        scored_movies = []

        for movie in movies:
            movie_title = movie[1]
            movie_genres = movie[5]
            movie_rating = movie[6]
            movie_year = movie[2]


            already_seen = False
            for r in all_rated:
                if r[3] == movie_title:
                    already_seen = True
                    break

            if already_seen:
                continue

            score = 0

            #genre match (+3)
            for genre in preferred_genres:
                if genre.lower() in movie_genres.lower():
                    score += 3
                    break

            #IMDb rating (+2 or +1)
            if movie_rating >= 7:
                score += 2

            elif movie_rating >= 5:
                score += 1

            #recent release
            if movie_year >= 2020:
                score += 1

            scored_movies.append({
                "title": movie_title,
                "genre": movie_genres,
                "rating": movie_rating,
                "score": score
            })

        #sort
        scored_movies.sort(key=lambda x: x["score"], reverse=True)

        return scored_movies[:limit]
