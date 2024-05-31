#!/usr/bin/python3
"""
Place class, a subclass of BaseModel class
"""
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os 

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'),
           primary_key=True, nullable=False),

    Column('amenity_id', String(60),
           ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
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

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete'
            )

        amenities = relationship(
            'Amenity',
            backref='place',
            secondary='place_amenity',
            viewonly=False
            )

    @property
    def reviews(self):
        """
        reviews method
        """
        from models.engine import file_storage
        from models.review import Review

        review_list = []
        all_reviews = file_storage.FileStorage.all(Review)
        for review in all_reviews.values():
            if isinstance(review, Review) and review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """
        returns the list of Amenity instances based
        on the attribute amenity_ids that contains
        all Amenity.id
        """
        from models.engine import file_storage
        from models.amenity import Amenity
        amenity_list = []
        all_amenitys = file_storage.FileStorage.all(Amenity)
        for amenity in all_amenitys.values():
            if isinstance(amenity, Amenity) and amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, obj=None):
        """
        method for adding an Amenity.id to the attribute amenity_ids
        """
        from models.amenity import Amenity
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
