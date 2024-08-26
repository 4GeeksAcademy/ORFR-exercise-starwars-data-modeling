import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    character_id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    character_url = Column(String(250), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    vehicle_id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250), nullable=False)
    vehicle_url = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    planet_url = Column(String(250), nullable=False)


class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    user_email = Column(String(250), nullable=False)
    user_password = Column(String(250), nullable=False)
    user_subscription_date = Column(DateTime, nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorites.favorite_id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship('Users', backref='favorites',uselist=False)

    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    vehicle = relationship('Vehicles', backref='favorites', lazy=True)

    planets_id = Column(Integer, ForeignKey('planets.planet_id'))
    planet = relationship('Planets', backref='favorites', lazy=True)

    character_id = Column(Integer, ForeignKey('characters.character_id'))
    character = relationship('Characters', backref='favorites', lazy=True)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
