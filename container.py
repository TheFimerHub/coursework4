from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDao
from service.auth import AuthService
from service.director import DirectorService
from service.genre import GenreService

from service.movie import MovieService
from service.user import UserService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)


user_dao = UserDao(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)
