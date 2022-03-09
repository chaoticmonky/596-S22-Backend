from datetime import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    messages = relationship("Message", back_populates="sender")
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    time = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, index=True)

    sender = relationship("User", back_populates="messages")

class DenseCaptionParent(Base):
    __tablename__ = "denseCaptionParent"

    id = Column(Integer, primary_key=True, index=True)
    imageName = Column(String, index=True)

    children = relationship("DenseCaptionChild", back_populates="parent")

class DenseCaptionChild(Base):
    __tablename__ = "denseCaptionChild"

    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String, index=True)
    score = Column(Float, index=True)
    bounding_x = Column(Float, index=True)
    bounding_y = Column(Float, index=True)
    bounding_w = Column(Float, index=True)
    bounding_h = Column(Float, index=True)
    parent_id = Column(Integer, ForeignKey("denseCaptionParent.id"))

    parent = relationship("DenseCaptionParent", back_populates="children")