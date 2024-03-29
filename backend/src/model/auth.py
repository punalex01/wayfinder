from sqlalchemy import inspect, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash

from src.model.user import User

from . import db


class UserAuth(db.Model):
    __tablename__ = "user_auth"

    # Auto Generated Fields:
    user_id = db.Column(db.Integer(), ForeignKey(User.id), primary_key=True)
    # The Date of the Instance Creation => Created one Time when Instantiation
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    # The Date of the Instance Update => Changed with Every Update
    updated = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    # Input by User Fields:
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    jwt_auth_active = db.Column(db.Boolean())

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

    def toDICT(self):
        cls_dict = {}
        cls_dict["_id"] = self.id
        cls_dict["email"] = self.email

        return cls_dict

    def toJSON(self):
        return self.toDICT()

    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.email


class JWTTokenBlocklist(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jwt_token = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"Expired Token: {self.jwt_token}"

    def save(self):
        db.session.add(self)
        db.session.commit()
