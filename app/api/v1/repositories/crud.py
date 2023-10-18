import json

from flask import request, jsonify

from app.services.app_exceptions import CustomException, AdNotFound
from app.services.crud_helper import create_ad_on_db, update_ad_on_db


def add_ad():
    action = 'POST_AD'
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException(' {}:درخواست نامعتبر است'.format(e), 406)
    print('req_data', req_data)
    try:
        insert_query_response = create_ad_on_db(
            text=req_data['text'],
            user_id=req_data['user_id']
        )
        print('insert_query_response', insert_query_response)
        if insert_query_response is not None:
            response_message = f"Ad posted successfully: the post is: {req_data['text']}"
            # admin_panel_transaction_logger(response_code=str(10001), status_code=200, action=action,
            #                                log_message=response_message
            #                                )
            return jsonify({"message": response_message, "ad_id": insert_query_response}), 200
    except Exception as e:
        raise CustomException(' {}:could not post ad'.format(e), 406)


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
        print('result',result)
        if result is None:
            print('result is none')
            AdNotFound.message = f"No update happened. The ad with {ad_id} id Does Not Exist."
            # ms_error_logger(
            #     response_code=str(10005),
            #     status_code=404,
            #     action=action,
            #     message=AdNotFound.message
            # )
            return jsonify(AdNotFound.message), 404
    except Exception as e:
        print(e)
        raise CustomException(' {}:اپدیت پست موفقیت آمیز نبود'.format(e), 406)

    message = f"ad updated successfully for user with id: {ad_id}"
    # admin_panel_transaction_logger(response_code=str(10007), action=action, message=message)
    return jsonify({"message": message})


def delete_ad():
    pass


def add_cm():
    pass


def get_ad_and_cms():
    pass
