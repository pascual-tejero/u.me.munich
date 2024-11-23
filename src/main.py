from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from survey import router as survey_router
from auth import router as auth_router
# from ai_recom import router as recommend_router


app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific frontend URLs in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(survey_router, prefix="/survey", tags=["Survey"])
# app.include_router(recommend_router, prefix="/recommend", tags=["RecommendationsAI"])