from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from openai import openai
from database import SessionLocal
from models import User, SurveyResponse

router = APIRouter()

# OpenAI Configuration
openai.api_key = "your-openai-api-key"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_recommendations(survey: SurveyResponse):
    # Create a prompt based on survey data
    preferences = [
        ("Indoor", survey.indoor),
        ("Outdoor", survey.outdoor),
        ("Cooking", survey.cooking),
        ("Music", survey.music),
        ("Conversations", survey.conversations),
        ("Reading", survey.reading),
        ("Traveling", survey.traveling),
        ("Other", survey.other),
    ]
    active_preferences = [pref[0] for pref in preferences if pref[1]]

    prompt = f"""
    You are a creative recommendation assistant. Based on the following preferences, suggest fun and personalized activities:
    Preferences: {', '.join(active_preferences)}.
    Be creative, especially if 'Other' is included!
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.8,
    )
    
    return response.choices[0].text.strip()

@router.get("/recommend/{user_email}")
def get_recommendations(user_email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    survey = db.query(SurveyResponse).filter(SurveyResponse.user_id == user.id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    recommendations = generate_recommendations(survey)
    return {"recommendations": recommendations}
