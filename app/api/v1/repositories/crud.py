import json

from flask import request, jsonify

from app.services.app_exceptions import CustomException, AdNotFound
from app.services.authorization import authorize
from app.services.crud_helper import create_ad_on_db, update_ad_on_db, delete_ad_on_db, create_cm_on_db


@authorize
def add_ad():
    action = 'POST_AD'
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException(' {}:درخواست نامعتبر است'.format(e), 406)
    try:
        insert_query_response = create_ad_on_db(
            text=req_data['text'],
            user_id=req_data['user_id']
        )
        if insert_query_response is not None:
            response_message = f"Ad posted successfully: the post is: {req_data['text']}"
            return jsonify({"message": response_message, "ad_id": insert_query_response}), 200
    except Exception as e:
        raise CustomException(' {}:could not post ad'.format(e), 406)


@authorize
def edit_ad(ad_id):
    action = 'EDIT_AD'
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException(' {}:درخواست نامعتبر است'.format(e), 406)
    try:
        result = update_ad_on_db(
            ad_id=ad_id,
            teext=req_data['text']
        )
        print('result', result)
        if result is None:
            print('result is none')
            AdNotFound.message = f"No update happened. The ad with {ad_id} id Does Not Exist."
            return jsonify(AdNotFound.message), 404
    except Exception as e:
        print(e)
        raise CustomException(' {}:اپدیت پست موفقیت آمیز نبود'.format(e), 406)

    message = f"ad updated successfully for user with id: {ad_id}"
    return jsonify({"message": message})


@authorize
def delete_ad(ad_id):
    action = 'delete_member'
    try:
        result = delete_ad_on_db(ad_id)

    except Exception as e:
        raise CustomException(' {}:حذف پست موفقیت آمیز نبود'.format(e), 406)

    if result is True:
        message = f"ad with {ad_id} deleted successfully"
        return jsonify({"message": message})

    elif result is False:
        AdNotFound.message = \
            f"No record was found for post with id: {ad_id}"

        return jsonify({"message": AdNotFound.message}), 404

    else:
        return jsonify(message=str(result))


@authorize
def add_cm():
    action = 'POST_COMMENT'
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException(' {}:درخواست نامعتبر است'.format(e), 406)
    try:
        insert_query_response = create_cm_on_db(
            text=req_data['text'],
            user_id=req_data['user_id'],
            ad_id=req_data['ad_id']
        )
        if insert_query_response is False:
            response_message = f"You have already added a comment to this post"
            return jsonify({"message": response_message}), 409

        if insert_query_response is not None and True:
            response_message = f"Comment added successfully"
            return jsonify({"message": response_message}), 200
    except Exception as e:
        raise CustomException(' {}:could not post cm'.format(e), 406)
    pass


def get_ad_and_cms():
    pass
