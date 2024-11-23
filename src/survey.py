from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SurveyResponse, User

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model for survey
class SurveyRequest(BaseModel):
    indoor: bool = False
    outdoor: bool = False
    sport: bool = False
    cooking: bool = False
    music: bool = False
    conversations: bool = False
    reading: bool = False
    traveling: bool = False

# @router.post("/survey/")
# @router.post("/")
# def submit_survey(request: SurveyRequest, user_email: str, db: Session = Depends(get_db)):
#     # Check if user exists
#     user = db.query(User).filter(User.email == user_email).first()
#     if not user:
#         raise HTTPException(status_code=400, detail="User not found")

#     # Prevent multiple survey submissions
#     if user.has_completed_survey:
#         raise HTTPException(status_code=400, detail="Survey already completed")

#     # Save survey response
#     survey_response = SurveyResponse(
#         user_id=user.id,
#         indoor_outdoor=request.indoor_outdoor,
#         sport=request.sport,
#         cooking=request.cooking,
#         music=request.music,
#         conversations=request.conversations,
#         reading=request.reading,
#         traveling=request.traveling,
#     )
#     db.add(survey_response)
#     db.commit()

#     # Mark survey as completed
#     user.has_completed_survey = True
#     db.commit()

#     return {"message": "Survey submitted successfully"}


@router.post("/")
def submit_survey(user_email: str, survey: SurveyRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    survey_response = SurveyResponse(user_id=user.id, **survey.dict())
    db.add(survey_response)
    db.commit()
    return {"message": "Survey results saved successfully"}


# @router.get("/survey/{user_email}")
@router.get("/{user_email}")
def get_survey_responses(user_email: str, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    # Fetch survey response
    survey = db.query(SurveyResponse).filter(SurveyResponse.user_id == user.id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    return {
        "indoor_outdoor": survey.indoor_outdoor,
        "sport": survey.sport,
        "cooking": survey.cooking,
        "music": survey.music,
        "conversations": survey.conversations,
        "reading": survey.reading,
        "traveling": survey.traveling,
    }






