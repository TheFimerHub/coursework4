import base64
import hashlib
import hmac

from dao.user import UserDao
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, data):
        data["password"] = self.generate_password(data["password"])
        return self.dao.create(data)

    def update(self, data, uid):
        user = self.get_one(uid)
        if data.get('password_1') is not None and data.get('password_2') is not None:
            if self.generate_password(data["password_1"]) == user.password:
                user.password = self.generate_password(data["password_2"])
            else:
                raise Exception

        if data.get('email') is not None:
            user.email = data["email"]
        if data.get('name') is not None:
            user.name = data["name"]
        if data.get('password') is not None:
            user.password = self.generate_password(data["password"])
        if data.get('surname') is not None:
            user.surname = data["surname"]
        if data.get('favorite_genre') is not None:
            user.favorite_genre = data["favorite_genre"]

        return self.dao.update(user)

    def delete(self, uid):
        return self.dao.delete(uid)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def compare_password(self, password_hash, other_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
