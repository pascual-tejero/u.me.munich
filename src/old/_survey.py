from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import SurveyResponse, User
import recommendations_class as Recommendations

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
    other: bool = False

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


@router.post("/{user_email}")
def submit_survey(user_email: str, survey: SurveyRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    survey_response = SurveyResponse(user_id=user.id, **survey.dict())
    db.add(survey_response)
    db.commit()
    # db.refresh()
    print(f"Survey saved: {survey_response}")
    return {"message": "Survey results saved successfully"}
    # return {"message": survey_response}


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
    print(f"Survey retrieved: {survey}")
    return {
        "indoor": survey.indoor,
        "outdoor": survey.outdoor,
        "sport": survey.sport,
        "cooking": survey.cooking,
        "music": survey.music,
        "conversations": survey.conversations,
        "reading": survey.reading,
        "traveling": survey.traveling,
        "other": survey.other,

    }



# @router.get("/recommendations/{user_email}")
@router.get("/recommendations/{user_email}")
def get_recommendations(user_email: str, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    
    # db.refresh(user)
    # Fetch survey response
    survey = db.query(SurveyResponse).filter(SurveyResponse.user_id == user.id).first()
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")

    # Generate recommendations
    recommendation_model = Recommendations.RecommendationModel(
        survey.indoor,
        survey.outdoor,
        sport=survey.sport,
        cooking=survey.cooking,
        music=survey.music,
        conversations=survey.conversations,
        reading=survey.reading,
        traveling=survey.traveling,
    )
    recommendations = recommendation_model.recommend()

    return {"recommendations": recommendations}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import google.generativeai as genai
from database import SessionLocal
from models import User, SurveyResponse
import os 

genai.configure(api_key=os.environ.get("API_KEY_Google"))
# print(os.environ.get("API_KEY_Google"))
genai.configure(api_key="AIzaSyARY6n7Vd-EEqRwjEY0IpNahNv0WXqSPvM")

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

    prompt = f"You are a creative recommendation assistant. Based on these preferences: {', '.join(preferences)}, suggest 3 fun, creative, and personalized activities. Be concise and helpful. If 'Other' is included, go wild!"
    

    try:
        
        model = genai.GenerativeModel()

        response = model.generate_content(prompt)
        # generated_text = response.content
        # return {"recommendations": generated_text}
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}") 

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# import google.generativeai as genai
# from database import SessionLocal
# from models import User, SurveyResponse
# import os 

# @router.get("/AIRecom/{user_email}")
# async def generate_recommendations(survey: SurveyResponse) -> str:
#     """
#     Generate recommendations using Gemini via google.generativeai.

#     Args:
#         survey (SurveyResponse): User's survey data.

#     Returns:
#         str: Generated recommendations.
#     """
#     survey_dict = {
#         "Indoor": survey.indoor,
#         "Outdoor": survey.outdoor,
#         "Cooking": survey.cooking,
#         "Music": survey.music,
#         "Conversations": survey.conversations,
#         "Reading": survey.reading,
#         "Traveling": survey.traveling,
#         "Other": survey.other,
#     }
#     preferences = [key for key, value in survey_dict.items() if value]

#     if not preferences:
#         return "You haven't provided any preferences. Please complete the survey."

#     prompt = (
#         f"You are a creative recommendation assistant. Based on these preferences: {', '.join(preferences)}, "
#         "suggest 3 fun, creative, and personalized activities. Be concise and helpful. If 'Other' is included, go wild!"
#     )

#     try:
#         response = genai.generate_text(prompt=prompt, temperature=0.7, max_output_tokens=256)
#         return response.result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}") 