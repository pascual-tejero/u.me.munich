from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SurveyResponse, User

# Router for survey-related endpoints
router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def submit_survey(question: str, answer: str, user_email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    survey_response = SurveyResponse(user_id=user.id, question=question, answer=answer)
    db.add(survey_response)
    db.commit()
    db.refresh(survey_response)
    return {"message": "Survey submitted successfully"}

@router.get("/")
def get_survey_responses(user_email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    responses = db.query(SurveyResponse).filter(SurveyResponse.user_id == user.id).all()
    return {"responses": [{"question": r.question, "answer": r.answer} for r in responses]}
