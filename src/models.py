import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Number
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    height = Column(Number(120), nullable=False)
    mass = Column(Number(120), nullable=False)
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
    cost_in_credits = Column(Number(120), nullable=False)
    length = Column(Number(120), nullable=False)
    max_atmosphering_speed = Column(Number(120), nullable=False)
    passangers = Column(Number(120), nullable=False)
    cargo_capacity = Column(Number(120), nullable=False)
    vehicle_class= Column(String(120), nullable=False)
    manufacturer= Column(String(120), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    rotation_period = Column(Number(120), nullable=False)
    orbital_period = Column(Number(120), nullable=False)
    diameter = Column(Number(120), nullable=False)
    climate = Column(String(120), nullable=False)
    gravity = Column(String(120), nullable=False)
    terrain = Column(String(120), nullable=False)
    surface_water = Column(Number(120), nullable=False)
    population = Column(Number(120), nullable=False)



    





class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
