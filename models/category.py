#!/usr/bin/python3
""" holds class User"""

import models
from models.basemodel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class Category(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'category'
    name = Column(String(50), nullable=False)
