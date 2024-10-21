from app import db
from datetime import datetime

class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_used = db.Column(db.DateTime)

    # Add a foreign key to the User model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # Define a relationship to the User model
    user = db.relationship('User', back_populates='pins')

    def __init__(self, category, value):
        self.category = category
        self.value = value
        self.date_used = None
