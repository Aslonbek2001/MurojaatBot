from sqlalchemy import Column, Integer,BigInteger, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
                                                     
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    tg_id = Column(BigInteger, unique=True, nullable=False, index=True)
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
    user_tg_id = Column(BigInteger, ForeignKey("users.tg_id", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="murojaatlar")


class Javob(Base):
    __tablename__ = "javoblar"

    id = Column(Integer, primary_key=True, index=True)
    murojaat_id = Column(Integer, ForeignKey("murojaatlar.id", ondelete="CASCADE"))
    javob = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    murojaat = relationship("Murojaat", lazy="subquery", passive_deletes=True)

