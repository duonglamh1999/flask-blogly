from flask import *
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'


connect_db(app)
db.create_all()

@app.route('/')
def root():
    return redirect("/user")

@app.route('/user')
def root():
    return redirect("/user")
