#!/usr/bin/python3
""" holds class cart"""

from models.basemodel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy.orm import relationship


class Cart(BaseModel, Base):
    """Representation of a cart"""
    __tablename__ = 'cart'
    quantity = Column(Integer, nullable=False)
