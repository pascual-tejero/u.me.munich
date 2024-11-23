from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from transformers import pipeline
from database import SessionLocal
from models import User, SurveyResponse

router = APIRouter()

# Initialize Hugging Face text generation pipeline
# You can replace "gpt2" with a larger model if needed, such as "EleutherAI/gpt-neo-1.3B"
# text_generator = pipeline("text-generation", model="gpt2")
text_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

def get_db():
    """Dependency to get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_recommendations(survey: SurveyResponse) -> str:
    """
    Generate recommendations using Hugging Face Transformers.

    Args:
        survey (SurveyResponse): User's survey data.

    Returns:
        str: Generated recommendations.
    """
    # Prepare survey data into a list of preferences
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

    # Create the prompt for text generation
    prompt = f"You are a creative recommendation assistant. Based on the following preferences, suggest fun and personalized activities:\nPreferences: {', '.join(preferences)}.\nBe creative, especially if 'Other' is included!"

    # Generate recommendations using the Hugging Face pipeline
    try:
        response = text_generator(prompt, max_length=150, num_return_sequences=1)
        recommendations = response[0]["generated_text"]
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@router.get("/recommend/{user_email}")
def get_recommendations(user_email: str, db: Session = Depends(get_db)):
    """
    API endpoint to fetch recommendations based on user survey data.

    Args:
        user_email (str): Email of the user.
        db (Session): Database session.

    Returns:
        dict: Generated recommendations.
    """
    # Fetch the user from the database
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch the user's survey responses
    survey = db.query(SurveyResponse).filter(SurveyResponse.user_id == user.id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    # Generate recommendations
    recommendations = generate_recommendations(survey)
    return {"recommendations": recommendations}
