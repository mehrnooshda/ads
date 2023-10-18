from app import db
from app.models.ad import Ad
from app.services.app_exceptions import CustomException, UnknownError


def create_ad_on_db(text, user_id):
    action = 'add_ad_on_db'
    try:
        ad = Ad(text=text, user_id=user_id)
        db.session.add(ad)
        db.session.commit()
        print(1)
        return ad.id

    except Exception as e:
        print(11,e)
        raise CustomException(' {}:error in posting ad'.format(e), 406)


def update_ad_on_db(ad_id, teext):
    action = 'edit_ad_on_db'
    try:
        ad = Ad.query.filter(Ad.id == ad_id).first()
        if not ad:
            return None
        print(1)
        ad.text = teext
        print(11)
        db.session.add(ad)
        print(111)

        db.session.commit()
        return True
    except Exception as e:
        # ms_error_logger(
        #     response_code=str(10008),
        #     status_code=422,
        #     action=action,
        #     message="{}".format(e)
        # )
        print(e, 'e dakhli da db')
        raise UnknownError