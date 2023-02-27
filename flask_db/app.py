from flask import Flask
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId # used to delete elements in DB


# ...

app = Flask(__name__)

client = MongoClient('localhost', 27017)  #mongo client-which you use to create a client object for a MongoDB

db = client.flask_db
todos = db.todos #todo is a collection
client = MongoClient('localhost', 27017, username='root', password='1234')

# ...


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)
#from pymongo import MongoClient


# ...

#deleting element in DB
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))