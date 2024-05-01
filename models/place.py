#!/usr/bin/python3
"""
Place class, a subclass of BaseModel class
"""
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.engine import file_storage
from models.amenity import Amenity
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                      )
class Place(BaseModel, Base):
    """
    A subclass of BaseModel class
    Public class attributes:
        city_id:             (str) will be City.id
        user_id:             (str) will be User.id
        name:                (str)
        description:         (str)
        number_rooms:        (int) 0
        number_bathrooms:    (int) 0
        max_guest:           (int) 0
        price_by_night:      (int) 0
        latitude:            (float) 0.0
        longitude:           (float) 0.0
        amenity_ids:         (list) will be Amenity.id
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship('Review', backref='place', cascade='all, delete')
    amenities = relationship('Amenity', backref='place', secondary='place_amenity', viewonly=False)

    @property
    def reviews(self):
        """
        reviews method
        """
        all_reviews = file_storage.FileStorage.all(self)
        return all_reviews

    @property
    def amenities(self):
        """
        returns the list of Amenity instances based
        on the attribute amenity_ids that contains
        all Amenity.id
        """
        return self.amenity_ids
    
    @amenities.setter
    def amenities(self, obj=None):
        """
        method for adding an Amenity.id to the attribute amenity_ids
        """
        if isinstance(obj, Amenity) and self.id == obj.id:
            self.amenity_ids.append(obj.id)
