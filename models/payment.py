#!/usr/bin/python3
""" holds class payment"""

from models.basemodel import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    """Representation of a payment"""
    __tablename__ = 'payment'
    payment_date = Column(DateTime, nullable=False,
                             default=datetime.utcnow)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),
                     nullable=False)
    order_id = Column(Integer, ForeignKey('order.id'),
                      nullable=False)
