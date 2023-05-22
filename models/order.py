#!/usr/bin/python3
""" holds class order"""

from models.basemodel import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """Representation of a order"""
    __tablename__ = 'order'
    total_price = Column(Float, nullable=False)
    order_date = Column(DateTime, nullable=False,
                        default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'),
                        nullable=False)
    items = relationship('OrderItem', backref='order',
                            lazy=True)
