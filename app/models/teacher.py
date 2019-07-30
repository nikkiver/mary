from app import  db
from sqlalchemy.dialects.mysql import VARCHAR

class Teacher(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name=db.Column(VARCHAR(40) , index=True )
    initials =db.Column(VARCHAR(10) )
    pno      =db.Column(VARCHAR(10) )
    dob      =db.Column(db.DateTime , nullable=False)
    subjects = db.Column(VARCHAR(100) , nullable=True)
    user_id  =db.Column(db.Integer , nullable=True)
    def __repr__(self):
        return "Teacher : {} , Initials : {}".format(self.name , self.initials)

