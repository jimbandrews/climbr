from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


class RopeGrades(Enum):
    five = '5.5'
    six = '5.6'
    seven = '5.7'
    eight = '5.8'
    nine = '5.9'
    ten = '5.10'
    eleven = '5.11'
    twelve = '5.12'
    thirteen = '5.13'


class BoulderGrades(Enum):
    VB = 'VB'
    V0 = 'V0'
    V1 = 'V1'
    V2 = 'V2'
    V3 = 'V3'
    V4 = 'V4'
    V5 = 'V5'
    V6 = 'V6'
    V7 = 'V7'
    V8 = 'V8'


class UserModel(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    boulder_max_grade = db.Column(db.String)
    boulder_reg_grade = db.Column(db.String)
    top_max_grade = db.Column(db.String)
    top_reg_grade = db.Column(db.String)
    lead_max_grade = db.Column(db.String)
    lead_reg_grade = db.Column(db.String)
    bio = db.Column(db.Text)
    city = db.Column(db.String)
    state = db.Column(db.String)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}:{self.email}"


class Gym(db.Model):
    __tablename__ = 'gym_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zipcode = db.Column(db.String)

    def __init__(self, name, street, city, state, zipcode):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __repr__(self):
        return f"{self.name}: {self.city}, {self.state}"
