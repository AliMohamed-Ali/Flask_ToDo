from flask import Flask, jsonify, request
from flask_restful import Api,Resource
from models import Todo,db

app= Flask(__name__)
todoApi= Api(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False



class todoRUD(Resource):
    def get(self,**kwargs):
        task = Todo.query.get(kwargs.get('id'))
        try:
            mytask = {
                'name': task.name,
                'id': task.id,
                'description': task.description
            }
            return mytask,200
        except Exception as e :
            print(e)
            return {'error': 'no such task'}


    def delete(self,**kwargs):
        task = Todo.query.get(kwargs.get('id'))
        try:
            db.session.delete(task)
            db.session.commit()
            return {'success': 'task deleted successfully '}
        except Exception as e:
            print(e)
            return {'error': 'no such task'}


    def patch(self,**kwargs):
        task = Todo.query.get(kwargs.get('id'))
        try:
            if request.form.get('name'):
                task.name=request.form.get('name')
            if request.form.get('description'):
                task.description=request.form.get('description')
            if request.form.get('finished'):
                task.finished=request.form.get('finished')
            db.session.commit()
            return {'success': 'task deleted successfully '}
        except Exception as e:
            print(e)
            return {'error': 'no such task'}

class todoLC(Resource):

    def post(self):
        mydata={
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'finished': False
        }
        task = Todo(**mydata)
        print(mydata)
        db.session.add(task)  
        db.session.commit()  
        return {'success': 'task added successfully '}
    def get(self):
        tasks= Todo.query.filter().all()
        newtask=[]
        for task in tasks:
            mytask = {
                'name': task.name,
                'id': task.id,
                'created_at': task.created_at,
                'description': task.description
            }
            newtask.append(mytask)
        return jsonify(newtask)



todoApi.add_resource(todoLC, '/api/v2/todo')
todoApi.add_resource(todoRUD, '/api/v2/todo/<int:id>')


db.init_app(app)

@app.before_first_request
def intiate_dbtablles():
    db.create_all()

app.run()
