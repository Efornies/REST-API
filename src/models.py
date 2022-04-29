from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    name =db.Column(db.String (250))
    lastname = db.Column(db.String(250))
    password = db.Column(db.String(250))
    email =db.Column(db.String(250), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username":self.username,
            "email": self.email,
            "name":self.name,
            "lastname":self.lastname, 

            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    eye_color = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "username":self.username,
            "email": self.email,
            "name":self.name,
            "lastname":self.lastname,
            "password":self.password,

            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    population = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    gravity = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "description": self.description,
            "population":self.population,
            "terrain":self.terrain,
            "gravity":self.gravity,

            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    passengers = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumibles = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "description": self.description,
            "passengers":self.passengers,
            "cargo_capacity":self.cargo_capacity,
            "consumibles":self.consumibles,

            # do not serialize the password, its a security breach
        }

    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Favorite_user=db.Column(db.Integer, db.ForeignKey("user.id"))
    Favorite_planets=db.Column(db.Integer, db.ForeignKey("planet.id"))
    Favorite_characters=db.Column(db.Integer, db.ForeignKey("character.id"))
    Favorite_vehicles=db.Column(db.Integer, db.ForeignKey("vehicle.id"))

    def serialize(self):
        return {
            "id": self.id,
            "favorite_user":self.Favorite_user,
            "favorite_planets": self.Favorite_planets,
            "favorite_characters":self.Favorite_characters,
            "favorites_vehicles":self.Favorite_vehicles,
      

            # do not serialize the password, its a security breach
        }

  