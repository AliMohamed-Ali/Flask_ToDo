from datetime import datetime

from flask_sqlalchemy import SQLAlchemy 

# db_antonsamir= SQLAlchemy() 
#instantiate sql alchemy class

# class todo(db_antonsamir.Model):

#     id= db_antonsamir.Column()


db = SQLAlchemy()  


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(125),nullable=False)
    description = db.Column(db.Text)
    finished = db.Column(db.Boolean)
    created_at=db.Column(db.DateTime)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.created_at= datetime.now()