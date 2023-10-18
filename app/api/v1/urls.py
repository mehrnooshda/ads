from app.api.v1 import api as api_v1
from app.api.v1.repositories.auth import login, register
from app.api.v1.repositories.crud import add_ad, edit_ad, delete_ad, add_cm, get_ad_and_cms

api_v1.add_url_rule('/ads/register', view_func=register, methods=['POST'])
api_v1.add_url_rule('/ads/login', view_func=login, methods=['POST'])
api_v1.add_url_rule('/ads/add/ad', view_func=add_ad, methods=['POST'])
api_v1.add_url_rule('/ads/edit/ad/<string:ad_id>', view_func=edit_ad, methods=['PUT'])
api_v1.add_url_rule('/ads/delete/ad', view_func=delete_ad, methods=['POST'])
api_v1.add_url_rule('/ads/add/comment', view_func=add_cm, methods=['POST'])
api_v1.add_url_rule('/ads/get/ad_and_comments', view_func=get_ad_and_cms, methods=['GET'])