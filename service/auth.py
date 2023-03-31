import jwt
import datetime
import calendar
from helpers.constants import PWD_SECRET, PWD_ALGORITHM
from service.user import UserService
from flask import abort


class AuthService:
    def __init__(self, service: UserService):
        self.service = service

    def generate_token(self, email, password, is_refresh=False):
        user = self.service.get_by_email(email)

        if user is None:
            abort(404)

        if not is_refresh:
            if not self.service.compare_password(user.password, password):
                abort(404)

        data = {
            "email": user.email,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, PWD_SECRET, algorithm=PWD_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, PWD_SECRET, algorithm=PWD_ALGORITHM)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=PWD_SECRET, algorithms=[PWD_ALGORITHM])
        email = data.get("email")

        return self.generate_token(email, None, is_refresh=True)
