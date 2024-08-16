from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
import enum

from ..db_setup import Base


class Role(enum.Enum):
    teacher = 1
    student = 2


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(Role), default=Role.student)

    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    owner = relationship("User", back_populates="profile")
