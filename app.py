# from flask import Flask, render_template, redirect, request, url_for
# from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from app import app
from app.models import User

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ac4.db"
# db = SQLAlchemy(app)

# class User(db.Model):
#     # nome da tabela
#     __tablename__ = "user"
#     # campos da tabela
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(50))
#     name = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     # post_user = db.relationship('Post', backref ='User', lazy=True)
#     # construtor da classe User
#     def __init__(self, user, password, name, email):
#         self.user = user
#         self.password = password
#         self.name = name
#         self.email = email

# class Follow(db.Model):
#     # nome da tabela
#     tablename="follow"
#     # campos da tabela
#     id =db.Column(db.Integer, primary_key=True, autoincrement=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     id_follower = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     follow_user = db.relationship("User", foreign_keys=[id_user])
#     follow_follower = db.relationship("User", foreign_keys=[id_follower])

#     # construtor da classe Follow
#     def __init__(self, id_user, id_follower):
#         self.id_user = id_user
#         self.id_folllower = id_follower

# esta classe irá criar a minha tabela
# class Post(db.Model):
#     # nome da tabela
#     __tablename__ = "post"
#     # campos da tabela
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     content = db.Column(db.String(100), unique=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     post_user = db.relationship("User", foreign_keys=[id_user])

#     # construtor da classe Post
#     def __init__(self, content, id_user):
#         self.content = content
#         self.id_user = id_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# @app.route("/")
# def index():
#     return render_template("index.html"), 200

# @app.route("/user")
# def index():
#     return render_template("user.html"), 200

# @app.route("/form_login", methods['POST'])
# def form_login():
#     login = request.form['txtLogin']
#     senha = request.form['txtSenha']

#     usuario = User.query.get(id)

#     if usuario.user == login and usuario.password == senha:
#         return redirect(url_for('user'))
#     else:
#         return render_template("index.html", mensagem="Login e/ou Senha inválido(s)!")

# if __name__ == "__main__":
#     # crio a tabela
#     db.create_all()
#     app.run(debug=True)


app.run(debug=True)
