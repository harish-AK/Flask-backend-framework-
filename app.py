from markupsafe import escape
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


@app.route('/capitalize/<word>/')#This new route has a variable section <word>. 
#This tells Flask to take the value from the URL and pass it to the view function
def capitalize(word):#The URL variable <word> passes a keyword argument to the capitalize() view function
    return '<h1>{}</h1>'.format(escape(word.capitalize())) # if user submits malicious js it will keep browser safe
#what ever we type in the url will be displayed in h1 format