import pytest

from unittest.mock import MagicMock

from dao.model.user import User
from dao.user import UserDao
from service.user import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDao(None)

    jonh = User(id=1, email='jonh', password='nwofn')
    kate = User(id=2, email='kate', password='nwlnsbwcofn')
    max = User(id=3, email='max', password='fdnwlfnw')

    user_dao.get_one = MagicMock(return_value=jonh)
    user_dao.get_by_username = MagicMock(return_value=jonh)
    user_dao.get_all = MagicMock(return_value=[jonh, kate, max])
    user_dao.create = MagicMock(return_value=User(id=3))
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()
    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)

        assert user is not None
        assert user.id is not None

    def test_get_all(self):
        users = self.user_service.get_all()

        assert len(users) > 0

    def test_create(self):
        user_d = {
            "email": "Ivan",
            'password': 'asd'
        }
        user = self.user_service.create(user_d)
        assert user.id is not None

    def test_delete(self):
        self.user_service.delete(1)

    def test_update(self):
        user_d = {
            "id": 3,
            "email": "Ivan",
            'password': 'asd'
        }

        self.user_service.update(user_d, user_d['id'])
