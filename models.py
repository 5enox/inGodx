from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    Email = Column(String, unique=True)
    FirstName = Column(String)
    LastName = Column(String)
    MobileNumber = Column(String)
    BirthDate = Column(String)
    Country = Column(String)
    State = Column(String)
    City = Column(String)
    Neighborhood = Column(String)
    Transport = Column(String)
    WorkedAsDelivery = Column(String)
    user = relationship("User", back_populates="data")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    user_type = Column(String)
    data_id = Column(Integer, ForeignKey('data.id'))

    data = relationship("Data", back_populates="user")
