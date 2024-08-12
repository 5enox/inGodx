from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    user_type: str
    full_name: Optional[str] = None


class UserSignIn(BaseModel):
    username: str
    password: str


class DeliveryGuy(BaseModel):
    first_name: str
    last_name: str
    email: str
    mobile_number: int
    birth_date: str
    country: str
    state: str
    city: str
    neighborhood: str
    transport: str
    worked_as_delivery: str
