from app import db, login_manager
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    # nome da tabela
    __tablename__ = "user"

    # campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False)
    followers = db.Column(db.Integer, nullable=False)
    following = db.Column(db.Integer, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Follow(db.Model):
    __tablename__ = "follow"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_follower = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, id_user, id_follower):
        self.id_user = id_user
        self.id_follower = id_follower


class Post(db.Model):
    # nome da tabela
    __tablename__ = "post"
    # campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(100), unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    post_user = db.relationship("User")

    # construtor da classe Post
    def __init__(self, user, password, name, email):
        self.user = user
        self.password = password
        self.name = name
        self.email = email


db.create_all()
