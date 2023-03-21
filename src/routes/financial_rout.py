from flask import Blueprint
import controllers.financial_controller as controller


financial_route = Blueprint("financial_route", __name__)
@financial_route.route("/markets", methods=["GET"])
def all_companies():
    return controller.get_all_markets()