from app import db


class Subject(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(20) , nullable=False)