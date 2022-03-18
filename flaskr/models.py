from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


class RopeGrades(Enum):
    five = "5.5"
    six = "5.6"
    seven = "5.7"
    eight = "5.8"
    nine = "5.9"
    ten = "5.10"
    eleven = "5.11"
    twelve = "5.12"
    thirteen = "5.13"


class BoulderGrades(Enum):
    VB = "VB"
    V0 = "V0"
    V1 = "V1"
    V2 = "V2"
    V3 = "V3"
    V4 = "V4"
    V5 = "V5"
    V6 = "V6"
    V7 = "V7"
    V8 = "V8"


class User(db.Model):
    __tablename__ = "user_table"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    boulder_max_grade = db.Column(db.String, nullable=True)
    boulder_reg_grade = db.Column(db.String, nullable=True)
    top_max_grade = db.Column(db.String, nullable=True)
    top_reg_grade = db.Column(db.String, nullable=True)
    lead_max_grade = db.Column(db.String, nullable=True)
    lead_reg_grade = db.Column(db.String, nullable=True)
    bio = db.Column(db.Text, nullable=True)
    city = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)

    # matches = db.relationship('Match', backref='climber', lazy=True)
    # swipes = db.relationship('Match', backref='climber', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}:{self.email}"


class Gym(db.Model):
    __tablename__ = "gym_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    street = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zipcode = db.Column(db.String)
    phone = db.Column(db.String)

    def __init__(self, name, street, city, state, zipcode, phone):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone

    def __repr__(self):
        return f"{self.name}: {self.city}, {self.state}"


# class Match(db.Model):
#     __tablename__ = "match_table"

#     id = db.Column(db.Integer, primary_key=True)
#     swiper = db.Column(db.Integer, db.ForeignKey('climber.id'), nullable=False)
#     swipee = db.Column(db.Integer, db.ForeignKey('climber.id'), nullable=False)
#     datetime = db.Column(db.DateTime, nullable=False, unique=False)