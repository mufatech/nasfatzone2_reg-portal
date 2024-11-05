# Modify user.py

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    zone = db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(20), nullable=False)  # 'Adult', 'Teen', 'Children', etc.
    age_range = db.Column(db.String(20), nullable=True)
    payment_date = db.Column(db.Date, nullable=False)
    registration_pin = db.Column(db.String(20), nullable=False)
    expectations = db.Column(db.Text, nullable=True)
    
    # Define a one-to-many relationship to the Pin model
    pins = db.relationship('Pin', back_populates='user')

    def __init__(self, first_name, last_name, number, email, zone, branch, gender, 
                 category, age_range, payment_date, registration_pin, expectations=None):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.zone = zone
        self.branch = branch
        self.gender = gender
        self.category = category
        self.age_range = age_range
        self.payment_date = payment_date
        self.registration_pin = registration_pin
        self.expectations = expectations
        