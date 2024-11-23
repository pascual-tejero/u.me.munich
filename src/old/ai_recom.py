from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import google.generativeai as genai
from database import SessionLocal
from models import User, SurveyResponse
import os 

router = APIRouter()

# Set up Generative AI API Key
# genai.configure(api_key="your-api-key")  # Use `PALM_API_KEY` from the environment if set
genai.configure(api_key=os.environ.get("API_KEY_Google"))


@router.get("/{user_email}")
def get_db():
    """Dependency to get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_recommendations(survey: SurveyResponse) -> str:
    """
    Generate recommendations using Gemini via google.generativeai.

    Args:
        survey (SurveyResponse): User's survey data.

    Returns:
        str: Generated recommendations.
    """
    # Convert survey data into preferences
    survey_dict = {
        "Indoor": survey.indoor,
        "Outdoor": survey.outdoor,
        "Cooking": survey.cooking,
        "Music": survey.music,
        "Conversations": survey.conversations,
        "Reading": survey.reading,
        "Traveling": survey.traveling,
        "Other": survey.other,
    }
    preferences = [key for key, value in survey_dict.items() if value]

    if not preferences:
        return "You haven't provided any preferences. Please complete the survey."

    # Create the prompt for Gemini
    prompt = (
        f"You are a creative recommendation assistant. Based on these preferences: {', '.join(preferences)}, "
        "suggest 3 fun, creative, and personalized activities. Be concise and helpful. you can also go wild if other is is true"
    )

    try:
        # Call the Generative AI model
        response = genai.generate_text(prompt=prompt, temperature=0.7, max_output_tokens=256)
        return response.result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")
