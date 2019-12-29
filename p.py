from flask import Flask,session,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xygkswomtxuojo:17ab83f42e9c703d07559a2657fcdac334aae047552aae2c126db65f3066357e@ec2-107-22-234-204.compute-1.amazonaws.com:5432/d8mga7c8qf7b3k'
@app.route('/')
def index():
    var =  Materia.query.all()
    return render_template("index.html",materias = var)
@app.route('/data/<name>')
def fun(name):
    session['name']=name
    q = jsonify(
        username=name
        )
    print(q)
    return q
app.secret_key = 'XXXXXXXXXXXXXX'
class Materia(db.Model):
    __tablename__="materias"
    id = db.Column(db.Integer,primary_key=True)
    Nombre = db.Column(db.String)
app.run(host="192.168.1.10")
    
