from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    murojaatlar = relationship("Murojaat", back_populates="user")

class Murojaat(Base):
    __tablename__ = "murojaatlar"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    your_position = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False)
    murojaat_type = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="murojaatlar")
