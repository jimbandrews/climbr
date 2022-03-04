from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    # boulder_max_grade = db.Column(db.String)
    # boulder_reg_grade = db.Column(db.String)
    # top_max_grade = db.Column(db.String)
    # top_reg_grade = db.Column(db.String)
    # lead_max_grade = db.Column(db.String)
    # lead_reg_grade = db.Column(db.String)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}:{self.email}"
