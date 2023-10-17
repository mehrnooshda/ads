import json

from flask import request, jsonify

from app.services.app_exceptions import CustomException
from app.services.crud_helper import create_ad_on_db


def add_ad():
    action = 'POST_AD'
    try:
        req_data = json.loads(request.data)
    except Exception as e:
        raise CustomException(' {}:درخواست نامعتبر است'.format(e), 406)
    print('req_data',req_data)
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


def edit_ad():
    pass

def delete_ad():
    pass

def add_cm():
    pass

def get_ad_and_cms():
    pass