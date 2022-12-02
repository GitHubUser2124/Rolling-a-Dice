class MovieReview:
    def __init__(self, movie, story, actors, music):
        #Movie Name
        self.movie_name = movie

        #Movie Ratings
        self.story_rating = story
        self.actors_rating = actors
        self.music_rating = music

        self.avg = int((self.story_rating + self.actors_rating + self.music_rating)/3) 

        self.myrating = {
            "Movie Name": self.movie_name,
            "Story Rating": self.story_rating,
            "Actor Rating": self.actors_rating,
            "Music Rating": self.music_rating,
            "Average Rating": self.avg
        }
    
    moviereviews = []

    review2 = MovieReview("Beautiful Sound", 5, 5, 5)