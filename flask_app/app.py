from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')   # another decorator  
def hello():  # hello is an view function 
    return '<h1>Hello, World!</h1>'
 #after this we can access "Hello,World!" from both 127.0.0.1:5000 and 127.0.0.1:5000/index

@app.route('/about/')              # another route  wihich is decorote into a new view function
def about():                       
    return '<h3>This is a Flask web application.</h3>'