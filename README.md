# U.Me.Munich

**Connecting People, Finding Companionship**

## Overview

U.Me.Munich is an innovative application designed to bring people together through shared activities, combating loneliness, and fostering a sense of companionship within the vibrant City of Munich. Developed as part of the HackaTUM 2024 challenge, this project aspires to make Munich a more inclusive and socially connected city.

<p align="center">
  <img src="assets/logo" alt="Logo" />
</p>

## Features

### 🌟 User-Centric Features

- **Personalized Survey**: Users complete a short survey about their interests and preferences (e.g., indoor/outdoor activities, cooking, music, etc.).
- **Activity Recommendations**: Based on survey responses, users receive tailored suggestions for fun and creative activities.
- **Companionship Matching**: The app helps users find others with similar interests for shared activities.
- Hosting events for those who like to organize!

### 🧠 Technology-Driven Features

- **AI-Powered Recommendations**: Using Google's Gemini AI, the app generates personalized and creative activity suggestions.
- **Secure User Management**: Built with FastAPI for secure registration, login, and data management.
- **Real-Time Engagement**: Users can explore new hobbies and connect with like-minded people in real-time.

### Become A Sponsor or Redeem Your Points Features
- Promoting government activities for a meet up location
- If you have businesses you can promote your businesses and be the sponsor if they meet up in your place!
- Users can redeem their points to have discounts or free access from sponsors!


## How It Works

1. **Register/Login**: Users sign up with their email and create a profile.
2. **Complete the Survey**: Users select their activity preferences.
3. **Get Recommendations**: Based on survey data, the app generates personalized activity suggestions using advanced AI.
4. **Connect and Act**: Users explore suggestions and find companions to join them in these activities.

## Technology Stack

### Backend

- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Google Generative AI (Gemini)**

### Frontend

- **TypeScript**
- **Vue**
- **CSS**

### Hosting

- Local development with potential integration for Google Cloud deployment.

## Setup and Installation

### Prerequisites

- Python 3.11+
- A virtual environment manager (e.g., Conda, venv)
- Google Cloud API Key for Generative AI - Gemini
- PostgreSQL for database setup

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-repo/U.Me.Munich.git 
    cd U.Me.Munich
    ```

2. **Set Up the Environment**

    ```bash
    conda env create -f src/backend_env.yml
    conda activate hackatum24  
    ```

3. **Configure Environment Variables**

    Create a `.env` file and add:

    ```env
    API_KEY_Google=your_google_api_key
    DATABASE_URL=sqlite:///./app.db  # Or PostgreSQL connection URL
    ```

4. **Run the Application**

    ```bash
    uvicorn main:app --reload
    ```

6. **Test the Endpoints**

    Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the FastAPI Swagger documentation.

<!-- ## API Endpoints

### Authentication

- `POST /auth/register/`: Register a new user.
- `POST /auth/login/`: Log in to the app.

### Survey

- `POST /survey/`: Submit a user’s activity preferences.
- `GET /survey/{user_email}`: Retrieve survey responses for a user.

### Recommendations

- `GET /recommendations/{user_email}`: Get personalized activity recommendations. -->

## Contributors (Team HackaTUM24)

- [**Cabrini Verren**](https://github.com/verren5)
- [**Malek Al Abed**](https://github.com/Malek-AlAbed)
- [**Mona Zhu**](https://github.com/MYZ1901)
- [**Pascual Tejero Cervera**](https://github.com/pascual-tejero)

## Future Goals

- **Expand Activity Database**: Add more activity categories and suggestions tailored for diverse interests.
- **Companion Matching**: Introduce a feature to connect users with similar preferences.
- **Mobile App Launch**: Build and deploy the NativeScript-powered frontend for iOS and Android.
- **Localization**: Translate the app into German for broader accessibility.

## Acknowledgments

Special thanks to:

- **HackaTUM 2024 Organizers**: For providing this incredible platform to innovate.
- **City of Munich**: For inspiring a challenge to fight loneliness and promote companionship.
