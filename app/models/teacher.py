from app import  db
from sqlalchemy.dialects.mysql import VARCHAR

class Teacher(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name=db.Column(VARCHAR(40) , index=True )
    initials =db.Column(VARCHAR(10) )
    pno      =db.Column(VARCHAR(10) )
    dob      =db.Column(db.DateTime , nullable=False)

    def __repr__(self):
        return "Teacher : {} , Initials : {}".format(self.name , self.initials)

