from sqlalchemy import desc

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie)

    def get_by_director_id(self, did):
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_by_genre_id(self, did):
        return self.session.query(Movie).filter(Movie.genre_id == did)

    def get_by_year(self, did):
        return self.session.query(Movie).filter(Movie.year == did)

    def get_by_status(self):
        return self.session.query(Movie).order_by(desc(Movie.year))

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, did):
        movie = self.get_one(did)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
