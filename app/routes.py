from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
  user = {'username': 'Anyama'}
  posts = [{
    'author': {'username':'Anyama'},
    'body': 'Beautiful Day in Moyo'
    },
    {
    'author': {'username': 'Robert'},
    'body': 'What a wonderfuly city, Arua!'
    },
    {
    'author': {'username': 'Wilfred'},
    'body': 'Great hopitality of West nilers'
    }]
  return render_template('index.html', user=user, title="Home", posts=posts)