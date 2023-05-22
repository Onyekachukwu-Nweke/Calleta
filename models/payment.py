#!/usr/bin/python3
""" holds class payment"""

from models.basemodel import BaseModel, Base
from os import getenv
from datetime import datetime
from sqlalchemy import Column, String, Text, Float, Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    """Representation of a payment"""
    __tablename__ = 'payment'
    payment_date = Column(DateTime, nullable=False,
                             default=datetime.utcnow)
    amount = Column(Float, nullable=False)
