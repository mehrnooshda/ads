from app import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))

    user = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('ad_user.id'))

    ad = db.relationship('Ad')
    ad_id = db.Column(db.Integer, db.ForeignKey('ad.id'))

    def __init__(self, text, user_id, ad_id):
        self.text = text
        self.user_id = user_id
        self.ad_id = ad_id