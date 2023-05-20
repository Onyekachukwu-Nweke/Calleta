#!/usr/bin/python3
""" holds class order"""

from models.basemodel import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """Representation of a order"""
    __tablename__ = 'order'
    quantity = Column(Integer, nullable=False)
