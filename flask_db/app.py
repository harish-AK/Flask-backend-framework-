from flask import Flask
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

# ...

app = Flask(__name__)

client = MongoClient('localhost', 27017)  #mongo client-which you use to create a client object for a MongoDB

db = client.flask_db
todos = db.todos #todo is a collection
client = MongoClient('localhost', 27017, username='root', password='1234')

# ...


@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')