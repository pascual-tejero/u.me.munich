class RecommendationModel:
    def __init__(self, indoor_outdoor, sport=False, cooking=False, music=False, conversations=False, reading=False, traveling=False):
        self.indoor_outdoor = indoor_outdoor.lower()
        self.preferences = {
            "sport": sport,
            "cooking": cooking,
            "music": music,
            "conversations": conversations,
            "reading": reading,
            "traveling": traveling,
        }

    def recommend(self):
        recommendations = []
        
        # Indoor Recommendations
        if self.indoor_outdoor == "indoor":
            if self.preferences["cooking"]:
                recommendations.append("Host a themed cooking night with friends.")
                recommendations.append("Take an online class to master gourmet cooking techniques.")
            
            if self.preferences["music"]:
                recommendations.append("Create a home karaoke setup and enjoy a music night.")
                recommendations.append("Explore digital audio workstations to produce your own music.")

            if self.preferences["reading"]:
                recommendations.append("Join an online book club or start journaling.")
                recommendations.append("Explore audiobooks and podcasts on topics you love.")

            if self.preferences["conversations"]:
                recommendations.append("Start a discussion group on current events or shared hobbies.")
                recommendations.append("Set up a virtual coffee meeting with friends far away.")
            
            # Combined indoor preferences
            if self.preferences["cooking"] and self.preferences["music"]:
                recommendations.append("Cook while listening to a curated playlist or live streams.")

            if self.preferences["reading"] and self.preferences["conversations"]:
                recommendations.append("Discuss a book or an article with a friend or a group online.")
        
        # Outdoor Recommendations
        elif self.indoor_outdoor == "outdoor":
            if self.preferences["sport"]:
                recommendations.append("Try adventurous activities like rock climbing or paddleboarding.")
                recommendations.append("Join a local recreational league for your favorite sport.")

            if self.preferences["music"]:
                recommendations.append("Look for open mic nights or outdoor jazz concerts.")
                recommendations.append("Explore street performers in a bustling city area.")

            if self.preferences["traveling"]:
                recommendations.append("Plan a weekend getaway to explore a new city or nature spot.")
                recommendations.append("Take a scenic train ride or road trip.")

            if self.preferences["conversations"]:
                recommendations.append("Attend a local cultural or networking event.")
                recommendations.append("Volunteer for a community event to meet new people.")
            
            # Combined outdoor preferences
            if self.preferences["sport"] and self.preferences["traveling"]:
                recommendations.append("Plan a trekking or cycling tour in the mountains or countryside.")
            
            if self.preferences["music"] and self.preferences["traveling"]:
                recommendations.append("Visit a famous music destination, like Nashville or Vienna.")

        # Recommendations not specific to indoor/outdoor
        if self.preferences["cooking"] and self.preferences["reading"]:
            recommendations.append("Explore cookbooks with unique recipes or food histories.")

        if self.preferences["sport"] and self.preferences["conversations"]:
            recommendations.append("Host a watch party for a big sports event with friends.")

        if self.preferences["traveling"] and self.preferences["reading"]:
            recommendations.append("Read travelogues or memoirs to inspire your next trip.")
        
        # Fallback Recommendations
        if not any(self.preferences.values()):
            recommendations.append("Explore a local museum or cultural center to learn something new.")
            recommendations.append("Try a mindfulness activity like yoga or meditation.")

        # Ensure unique recommendations
        recommendations = list(set(recommendations))
        
        return recommendations
