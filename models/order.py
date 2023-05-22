#!/usr/bin/python3
""" holds class order"""

from models.basemodel import BaseModel, Base
from os import getenv
from datetime import datetime
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """Representation of a order"""
    __tablename__ = 'order'
    total_price = Column(Float, nullable=False)
    order_date = Column(DateTime, nullable=False,
                        default=datetime.utcnow)
