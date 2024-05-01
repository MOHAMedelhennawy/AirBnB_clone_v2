#!/usr/bin/python3
"""
Amenity class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"), nullable=False, primary_key=True),
    Column("amenity_id", String(60), ForeignKey("amenities.id"), nullable=False, primary_key=True)
)
class Amenity(BaseModel):
    """
    A subclass of BaseModel class
    Public class attribute:
        name: (str)
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
