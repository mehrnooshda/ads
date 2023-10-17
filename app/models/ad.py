from app import db


class Ad(db.Model):
    __tablename__ = 'ad'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))

    user = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('ad_user.id'))

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id