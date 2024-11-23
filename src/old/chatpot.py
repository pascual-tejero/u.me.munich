import openai
import env 

# Set up the OpenAI API key
openai.api_key = env.OPENAI_API_KEY

def get_recommendations_from_chatbot(preferences: dict) -> str:
    """
    Use OpenAI API to get recommendations based on user preferences.

    Args:
        preferences (dict): User preferences (e.g., {"indoor": 1, "outdoor": 0, ...}).

    Returns:
        str: Recommendations as a natural language response.
    """
    prompt = f"""
    You are a recommendation assistant. Recommend activities to a user based on their preferences.
    
    Preferences:
    - Indoor: {"Yes" if preferences.get("indoor") else "No"}
    - Outdoor: {"Yes" if preferences.get("outdoor") else "No"}
    - Cooking: {"Yes" if preferences.get("cooking") else "No"}
    - Music: {"Yes" if preferences.get("music") else "No"}
    - Conversations: {"Yes" if preferences.get("conversations") else "No"}
    - Reading: {"Yes" if preferences.get("reading") else "No"}
    - Traveling: {"Yes" if preferences.get("traveling") else "No"}
    
    Provide a friendly, personalized recommendation.
    """
    
    # Call OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use GPT-3.5 or GPT-4
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    
    return response.choices[0].text.strip()
