import pytest
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    nolan = Director(id=1, name='Кристофер Нолан')
    tarantino = Director(id=2, name='Квентин Тарантино')
    richi = Director(id=3, name='Гай Ричи')

    director_dao.get_one = MagicMock(return_value=nolan)
    director_dao.get_all = MagicMock(return_value=[nolan, tarantino, richi])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        new_director = {"name": "Джеймс Ган", }
        director = self.director_service.create(new_director)

        assert director is not None
        assert director.id is not None

    def test_delete(self):
        director_removed = self.director_service.delete(1)

        assert director_removed is None

    def test_update(self):
        director_updated = {"id": 3, "name": "Андрей Тарковский"}
        self.director_service.update(director_updated)