from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    FirstName: str
    LastName: str
    Email: str
    MobileNumber: str
    BirthDate: str
    Country: str
    State: str
    City: str
    Neighborhood: str
    Transport: str
    WorkedAsDelivery: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
