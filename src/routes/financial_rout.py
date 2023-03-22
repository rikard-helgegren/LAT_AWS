from flask import Blueprint
import controllers.financial_controller as controller
from flask import request
from flask import json


financial_route = Blueprint("financial_route", __name__)
@financial_route.route("/markets", methods=["GET"])
def all_companies():
    return controller.get_all_markets()


@financial_route.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return return_data(json)
    else:
        return 'Content-Type not supported!'
    
def return_data(json):
    return_string = ""

    for key in json.keys():

        if json[key] == "sweden":
            return_string = return_string + json[key] + ": mean:1.12, median:1.13 \n"
        if json[key] == "USA":
            return_string = return_string + json[key] + ": mean:1.07, median:1.08 \n"

    return return_string
