

from . import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(18),nullable=False)
    email = db.Column(db.String(18),nullable=False, unique=True)
