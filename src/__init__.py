from .config import DBConnection
from .entities import User as UserModel


class UserRepository:
    def insert(self, name):
        with DBConnection() as db:
            new_user = UserModel(name=name)
            db.session.add(new_user)
            db.session.commit()
