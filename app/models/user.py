from datetime import datetime
from app import  db


class User(db.Model):
    id = db.Column(db.Integer , primary_key=True )
    username = db.Column(db.String(50) , index=True ,nullable=False ,unique=True)
    password = db.Column(db.String(100) , nullable=False)
    role = db.Column(db.String(30) , nullable=False)
    status = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return "User name = {}".format(self.username)
