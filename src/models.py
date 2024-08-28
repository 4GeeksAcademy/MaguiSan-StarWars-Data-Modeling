import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorite_character = Table('favorite_character', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('character.id'), primary_key=True)
)
favorite_vehicle = Table('favorite_vehicle', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('vehicle_id', Integer, ForeignKey('vehicle.id'), primary_key=True)
)
favorite_planet = Table('favorite_planet', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), primary_key=True)
)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    favorite_character = relationship('Character', secondary = favorite_character, lazy='subquery', backref = 'users')
    favorite_vehicle = relationship('Vehicle', secondary = favorite_vehicle, lazy='subquery', backref = 'users')
    favorite_planet = relationship('Planet', secondary = favorite_planet, lazy='subquery', backref = 'users')
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    height = Column(String(120), nullable=False)
    mass = Column(String(120), nullable=False)
    hair_color = Column(String(120), nullable=False)
    skin_color = Column(String(120), nullable=False)
    eye_color = Column(String(120), nullable=False)
    birth_year = Column(String(120), nullable=False)
    gender = Column(String(120), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    cost_in_credits = Column(String(120), nullable=False)
    length = Column(String(120), nullable=False)
    max_atmosphering_speed = Column(String(120), nullable=False)
    passangers = Column(String(120), nullable=False)
    cargo_capacity = Column(String(120), nullable=False)
    vehicle_class= Column(String(120), nullable=False)
    manufacturer= Column(String(120), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    rotation_period = Column(String(120), nullable=False)
    orbital_period = Column(String(120), nullable=False)
    diameter = Column(String(120), nullable=False)
    climate = Column(String(120), nullable=False)
    gravity = Column(String(120), nullable=False)
    terrain = Column(String(120), nullable=False)
    surface_water = Column(String(120), nullable=False)
    population = Column(String(120), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
