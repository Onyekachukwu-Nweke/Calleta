#!/usr/bin/python3
""" holds class category"""

import models
from models.basemodel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Representation of a category """
    __tablename__ = 'category'
    name = Column(String(50), nullable=False)
