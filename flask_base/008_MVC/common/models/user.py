# coding: utf-8
# from sqlalchemy import Column, DateTime, Integer, JSON, LargeBinary, SmallInteger, String, Text
# from sqlalchemy.schema import FetchedValue
# from sqlalchemy.dialects.mysql.enumerated import ENUM
# from flask_sqlalchemy import SQLAlchemy
from application import db

# db = SQLAlchemy()




class User(db.Model):
    __tablename__ = 'user'

    Host = db.Column(db.String(255, 'ascii_general_ci'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    User = db.Column(db.String(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
    User_attributes = db.Column(db.JSON)
