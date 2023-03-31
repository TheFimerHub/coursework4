from flask_restx import Resource, Namespace
from container import movie_service
from flask import request
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    # @auth_required
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        status = request.args.get('status')
        page = request.args.get('page')
        filters = {
            "director_id": director_id,
            "genre_id": genre_id,
            "year": year,
            "status": status,
            "page": page
        }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    # @auth_required
    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "Created", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    # @auth_required
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    # @auth_required
    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update(req_json)
        return "Movie was updated", 204

    # @auth_required
    def patch(self, mid):
        req_json = request.json
        req_json["id"] = mid

        movie_service.update_partial(req_json)
        return "Partial update of movie", 204

    # @auth_required
    def delete(self, mid):
        movie_service.delete(mid)
        return "Movie was deleted", 204
