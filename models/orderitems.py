#!/usr/bin/python3
""" holds class order_item"""

from models.basemodel import BaseModel, Base
from os import getenv
from datetime import datetime
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class OrderItem(BaseModel, Base):
    """Representation of a order_item"""
    __tablename__ = 'order_item'
    quantity = Column(Integer, nullable=False)
    # item_price = Column(Float, nullable=False)
