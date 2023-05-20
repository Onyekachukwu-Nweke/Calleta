#!/usr/bin/python3
""" holds class User"""

import models
from models.basemodel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class Product(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'product'
    name = Column(String(128), nullable=False)
    desc = Column(Text)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    # places = relationship("Place", backref="user")
    # reviews = relationship("Review", backref="user")
