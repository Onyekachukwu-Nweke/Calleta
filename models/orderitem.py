#!/usr/bin/python3
""" holds class order_item"""

from models.basemodel import BaseModel, Base
from os import getenv
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class OrderItem(BaseModel, Base):
    """Representation of a order_item"""
    __tablename__ = 'order_item'
    quantity = Column(Integer, nullable=False)
    order_id = Column(Integer, ForeignKey('order.id'),
                         nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'),
                           nullable=False)
