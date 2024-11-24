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
        prompt = "You are my boredom-busting assistant, a fun and creative activities guru! I have no specific preferences, so go wild with your recommendations! Think outside the box and suggest anything from thrilling adventures to quirky indoor activities. Be imaginative, bold, and fun. And remember—go crazy!"
    else:
        prompt = f"You are my boredom-busting and loneliness-curing assistant, here to recommend fun and creative activities! Based on these preferences: {', '.join(preferences)}, suggest {len(preferences)} personalized and engaging activities tailored for people in Munich. Offer a diverse mix of ideas that resonate with these interests, blending indoor and outdoor options. Where possible, combine preferences for unique and exciting experiences. Include specific locations, events, or highlights in Munich, especially those happening within the next day. If 'Go Crazy' is included, push the boundaries with bold, unconventional suggestions, mixing them with other preferences for an adventurous twist. Keep your suggestions concise, engaging, and packed with fun!"
        
    try:
        model = genai.GenerativeModel()
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}") 