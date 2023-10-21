from app import db
from app.models.ad import Ad
from app.models.comment import Comment
from app.services.app_exceptions import CustomException, UnknownError


def create_ad_on_db(text, user_id):
    action = 'add_ad_on_db'
    try:
        ad = Ad(text=text, user_id=user_id)
        db.session.add(ad)
        db.session.commit()
        return ad.id

    except Exception as e:
        raise CustomException(' {}:error in posting ad'.format(e), 406)


def update_ad_on_db(ad_id, teext):
    action = 'edit_ad_on_db'
    try:
        ad = Ad.query.filter(Ad.id == ad_id).first()
        if not ad:
            return None
        ad.text = teext
        db.session.add(ad)
        db.session.commit()
        return True
    except Exception as e:
        raise UnknownError


def delete_ad_on_db(ad_id):
    action = 'delete_ad_on_db'
    try:
        ad = Ad.query.filter(Ad.id == ad_id).first()
        if ad:
            db.session.delete(ad)
            db.session.commit()
            return True

        else:
            return False
    except Exception as e:
        raise UnknownError


def create_cm_on_db(text, user_id, ad_id):
    action = 'add_ad_on_db'
    try:

        comment = Comment(text=text, user_id=user_id, ad_id=ad_id)
        exists = Comment.query.filter(Comment.user_id == user_id, Comment.ad_id == ad_id).first()
        if exists:
            return False
        db.session.add(comment)
        db.session.commit()
        return True

    except Exception as e:
        raise CustomException(' {}:error in posting cm'.format(e), 406)
