from datetime import datetime
from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'ad_user'

    #todo email validator while login
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    hashed_password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password


    @classmethod
    def hash_password(cls, password):
        return generate_password_hash(password)


    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if not username or not password:
            return None

        user = cls.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user