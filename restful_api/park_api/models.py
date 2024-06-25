from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    api_key = db.Column(db.String(150))
    

class Park(db.Model):
    __tablename__ = 'parks'
    park_id = db.Column(db.Integer, primary_key=True)
    park_code = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)

class Camp(db.Model):
    __tablename__ = 'camps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    park_code = db.Column(db.String, db.ForeignKey('parks.park_code'))
    state = db.Column(db.String)
    longitude = db.Column(db.Integer)
    latitude = db.Column(db.Integer)
    totalSites = db.Column(db.Integer)
    tentOnly = db.Column(db.Integer)
    electricalHookups = db.Column(db.Integer)
    showers = db.Column(db.String)
    dumpStation = db.Column(db.String)
    host = db.Column(db.String)
    potableWater = db.Column(db.String)
    firewoodForSale = db.Column(db.String)
    reservationUrl = db.Column(db.String)
    park = db.relationship("Park")
