from datetime import datetime
from sqlite3 import Timestamp
from typing import List, Optional, Dict
from xmlrpc.client import DateTime
from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, true

# Item Models
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# User Models
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

# Message Models
class MessageCreate(BaseModel):
    text: str
    sender_id: int
    recipient_id: int

class Message(BaseModel):
    id: int
    text: str
    time: datetime = datetime.now()
    sender_id: int
    recipient_id: int

    class Config:
        orm_mode = True

######### Recognized Plates ###############
class RecognizedPlate(BaseModel):
    id: int
    license: str
    time: TIMESTAMP
    footage_id: int

    class Config:
        orm_mode = True

############ License Plate Footage #############

class LicenseFootageBase(BaseModel):
    link: str

class CreateLicenseFootage(LicenseFootageBase):
    pass 

class LicenseFootage(BaseModel):
    id: int
    filename: str
    date_uploaded = datetime.now()
    recognized_plates: List(RecognizedPlate)

    class Config:
        orm_mode = True