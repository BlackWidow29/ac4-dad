from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # nome da tabela
    __tablename__ = "user"

    # campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
