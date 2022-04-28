from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    name =db.Column(db.String (250))
    lastname = db.Column(db.String(250))
    password = db.Column(db.String(250))
    email =db.Column(db.String(250), nullable=False)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    eye_color = db.Column(db.Integer)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    population = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    gravity = db.Column(db.Integer)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    passengers = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumibles = db.Column(db.Integer)
   
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Favorite_user=db.Column(db.Integer, db.ForeignKey("user.id"))
    Favorite_planets=db.Column(db.Integer, db.ForeignKey("planet.id"))
    Favorite_characters=db.Column(db.Integer, db.ForeignKey("character.id"))
    Favorite_vehicles=db.Column(db.Integer, db.ForeignKey("vehicle.id"))