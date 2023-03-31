from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from container import director_service
from flask import request

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    # @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    # @auth_required
    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "Successfully", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    # @auth_required
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    # @auth_required
    def put(self, did):
        req_json = request.json
        req_json['id'] = did

        director_service.update(req_json)
        return "Director was updated", 204

    # @auth_required
    def delete(self, did):
        director_service.delete(did)
        return "Movie was deleted", 204
