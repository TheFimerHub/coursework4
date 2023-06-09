from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        did = data.get('id')
        director = self.get_one(did)

        director.name = data.get('name')

        self.dao.update(director)

    def delete(self, did):
        self.dao.delete(did)
