#!/usr/bin/python3
""" holds class cart"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Cart(BaseModel, Base):
    """Representation of a cart"""
    __tablename__ = 'cart'
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),
                        nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'),
                           nullable=False)
