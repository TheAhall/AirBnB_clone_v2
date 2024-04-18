#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                              Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    else:
        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances
            based on the attribute amenity_ids that contains all Amenity.id
            linked to the Place"""
            from models import storage
            amenity_objs = []
            for amenity_id in self.amenity_ids:
                key = "Amenity." + amenity_id
                amenity_objs.append(storage.all()["Amenity"][key])
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute that handles append method for adding
            an Amenity.id to the attribute amenity_ids"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
