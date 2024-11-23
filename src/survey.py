from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SurveyResponse, User
import google.generativeai as genai
import os 

genai.configure(api_key="AIzaSyARY6n7Vd-EEqRwjEY0IpNahNv0WXqSPvM")

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

    sporty: bool = False
    party: bool = False
    nature: bool = False
    cafe_hopping: bool = False
    cooking: bool = False
    cinema: bool = False
    walking: bool = False
    reading: bool = False
    gardening: bool = False
    conversation: bool = False
    go_crazy: bool = False


@router.post("/{user_email}")
def submit_survey(user_email: str, survey: SurveyRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    survey_response = SurveyResponse(user_id=user.id, **survey.dict())
    db.add(survey_response)
    db.commit()
    # db.refresh()
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

        "sporty": survey.sporty,
        "party": survey.party,
        "nature": survey.nature,
        "cafe_hopping": survey.cafe_hopping,
        "cooking": survey.cooking,
        "cinema": survey.cinema,
        "walking": survey.walking,
        "reading": survey.reading,
        "gardening": survey.gardening,
        "conversation": survey.conversation,
        "go_crazy": survey.go_crazy,
    }



@router.get("/gen/{user_email}")
def generate_recoms( user_email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    # Fetch survey response
    survey = db.query(SurveyResponse).filter(SurveyResponse.user_id == user.id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")


    survey_dict = {
        "Sporty": survey.sporty,
        "Party": survey.party,
        "Nature": survey.nature,
        "Cafe Hopping": survey.cafe_hopping,
        "Cooking": survey.cooking,
        "Cinema": survey.cinema,
        "Walking": survey.walking,
        "Reading": survey.reading,
        "Gardening": survey.gardening,
        "Conversation": survey.conversation,
        "Go Crazy": survey.go_crazy

    }
    preferences = [key for key, value in survey_dict.items() if value]

    if not preferences:
        survey.go_crazy = True 
        prompt = f"You are my bored-state killer that you act as a fun and creative activities recommendation assitance. Since I do not have any preferences, go wild with the recommendations! It can be anything from indoor to outdoor activities. Be creative and fun! And remember, go crazy!"
        # return "You haven't provided any preferences. Please complete the survey."
    else:
        prompt = f"You are my bored-state killer that you act as a fun and creative activities recommendation assitance. Based on these preferences: {', '.join(preferences)}, suggest {len(preferences)} fun, creative, and personalized activities. Be concise and helpful. Try to mix between the acitivites if possible. If go_crazy is included, go wild with the recommendations! if there are other activities along with go_crazy, make sure to go wild with them as well"
        
    try:
        model = genai.GenerativeModel()
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}") 
