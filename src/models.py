from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    has_completed_survey = Column(Boolean, default=False)

    # Relationship to Survey
    survey = relationship("SurveyResponse", back_populates="user", uselist=False)

class SurveyResponse(Base):
    __tablename__ = "survey_responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    sporty = Column(Boolean, default=False)
    party = Column(Boolean, default=False)
    nature = Column(Boolean, default=False)
    cafe_hopping = Column(Boolean, default=False)
    cooking = Column(Boolean, default=False)
    cinema = Column(Boolean, default=False)
    walking = Column(Boolean, default=False)
    reading = Column(Boolean, default=False)
    gardening = Column(Boolean, default=False)
    conversation = Column(Boolean, default=False)
    go_crazy = Column(Boolean, default=False)

    user = relationship("User", back_populates="survey")