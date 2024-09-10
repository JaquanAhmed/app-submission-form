from flask_login import UserMixin

from db import get_db

class User(UserMixin):
    def __init__(self, id_, fname, lname, email):
        self.id = id_
        self.fname = fname
        self.lname = lname
        self.email = email

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], fname=user[1], lname=user[2], email=user[3]
        )
        return user

    @staticmethod
    def create(id_, fname, lname, email):
        db = get_db()
        db.execute(
            "INSERT INTO user (id, fname, lname, email) "
            "VALUES (?, ?, ?, ?)",
            (id_, fname, lname, email),
        )
        db.commit()