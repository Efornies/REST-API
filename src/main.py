"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Vehicle, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/user", methods=["POST"])
def create_user():
    body_name = request.json.get("name")
    user = User(name=body_name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"name": user.name, "msg": "creado el usuario con id" + str(user.id)}), 200


@app.route('/users', methods=['GET'])
def handle_hello():
    get_user= User.query.all() 
    users = list(map(lambda a:a.serialize(),get_user))
    return jsonify(users)


@app.route('/planets', methods=['GET'])
def handle_planets():
    get_planets= Planet.query.all() 
    planets = list(map(lambda a:a.serialize(),get_planets))
    return jsonify(planets)

    
@app.route('/planet/<int:id>', methods=['GET'])
def handle_planet(id):
    get_planet= Planet.query.get(id) 
    return jsonify(get_planet.serialize())

@app.route('/vehicles', methods=['GET'])
def handle_vehicles():
    get_vehicles= Vehicle.query.all() 
    Vehicles = list(map(lambda a:a.serialize(),get_vehicles))
    return jsonify(vehicles)

    
@app.route('/vehicle/<int:id>', methods=['GET'])
def handle_vehicle(id):
    get_vehicle= Vehicle.query.get(id) 
    return jsonify(get_vehicle.serialize())


    
@app.route('/favorite/<int:id>', methods=['GET'])
def handle_favorite(id):
    get_favorte= Favorites.query.get(id) 
    return jsonify(get_favorite.serialize())

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
