from sqlalchemy import Column, Integer, String
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    FirstName = Column(String, index=True)
    LastName = Column(String, index=True)
    Email = Column(String, unique=True, index=True)
    MobileNumber = Column(String, index=True)
    BirthDate = Column(String)
    Country = Column(String)
    State = Column(String)
    City = Column(String)
    Neighborhood = Column(String)
    Transport = Column(String)
    WorkedAsDelivery = Column(String)
