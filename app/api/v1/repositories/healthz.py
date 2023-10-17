# -*- coding: UTF-8 -*-
from flask import jsonify


def ads_health_check():
    return jsonify({"success": True})