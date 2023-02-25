from flask import Flask, render_template
import datetime
app1 = Flask(__name__)


@app1.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app1.route('/about/')
def about():
    return render_template('about.html')