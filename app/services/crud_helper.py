from app import db
from app.models.ad import Ad
from app.services.app_exceptions import CustomException


def create_ad_on_db(text, user_id):
    action = 'add_member_on_db'
    try:

        ad = Ad(text=text, user_id=user_id)
        db.session.add(ad)
        db.session.commit()
        print(1)
        return ad.id

    except Exception as e:
        print(11,e)
        raise CustomException(' {}:error in posting ad'.format(e), 406)