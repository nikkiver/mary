from app import app , db
from datetime import datetime

class Collectionrecord(db.Model):
    id = db.Column(db.Integer , primary_key=True )
    description=db.Column(db.String(100) , nullable=False)
    collectiondate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    standard = db.Column(db.String(10) , nullable=False  )
    subject =db.Column(db.String(20) , nullable= False)
    teacherinitials =db.Column(db.String(10) , nullable=False)
    defaulters = db.relationship('Defaulter' , backref="collection" ,cascade="all, delete-orphan")

    def __init__(self , description ,collectiondate , standard ,teacherinitials , subject):
        self.description =description
        self.collectiondate = collectiondate
        self.standard= standard
        self.teacherinitials = teacherinitials
        self.subject = subject

class Defaulter(db.Model):
    id = db.Column(db.Integer , primary_key=True )
    admno =         db.Column(db.Integer , nullable=False)
    name =         db.Column(db.String(10) , nullable=False)
    status =        db.Column(db.String(10) , nullable=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('collectionrecord.id'))
    