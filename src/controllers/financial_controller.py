from flask.json import jsonify
import services.financial_service as service

#validera data fron import
#validera atherization
#ratt felmedelande



def get_all_markets():
    markets = service.get_markets()
    return jsonify(markets)


