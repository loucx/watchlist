from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',name = name, movies=movies)


name = 'Loucx'
movies = [
    {'title':'排球少年','year':'2016'},
    {'title':'强风吹拂','year':'2018'},
    {'title':'乒乓','year':'2014'},
    {'title':'樱桃小丸子','year':'1990'},
    {'title':'灌篮高手','year':'1993'},
]