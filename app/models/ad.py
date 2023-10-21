import marshmallow_sqlalchemy

from app import db, ma
from app.models.comment import Comment


class Ad(db.Model):
    __tablename__ = 'ad'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))

    user = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('ad_user.id'))

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id


class AdSchema(ma.SQLAlchemyAutoSchema):
    ads_and_cms = ma.Method('get_cms')

    class Meta:
        model = Ad

    def get_cms(self, obj):
        ads_cms = db.session.query(Ad).join(Comment).filter(Ad.id == obj.id).all()
        return ads_cms
