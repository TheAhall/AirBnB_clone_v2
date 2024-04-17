#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
