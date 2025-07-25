# main.py

import openai
from config import OPENAI_API_KEY

def get_user_preferences():
    print("👋 Welcome to the AI Date Planner!")
    location = input("Enter your city or zip code: ")
    budget = input("What's your budget (e.g., $, $$, $$$)? ")
    food = input("Any preferred cuisine or dining experience? ")
    vibe = input("Do you want something romantic, fun, adventurous? ")
    activity = input("Any specific activity (movie, hike, museum)? ")
    time = input("Evening, afternoon, or weekend plan? ")
    
    return {
        "location": location,
        "budget": budget,
        "food": food,
        "vibe": vibe,
        "activity": activity,
        "time": time
    }

def generate_ai_plan(preferences):
    openai.api_key = OPENAI_API_KEY

    prompt = f"""
You are a creative and thoughtful date planning assistant.
Given the user's preferences below, generate a fun, romantic, and personalized date night plan.

Preferences:
- Location: {preferences['location']}
- Budget: {preferences['budget']}
- Cuisine: {preferences['food']}
- Vibe: {preferences['vibe']}
- Activity: {preferences['activity']}
- Time: {preferences['time']}

Respond with a short 3-step plan, written in a friendly tone.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",  # use "gpt-3.5-turbo" if you don’t have access to GPT-4
        messages=[
            {"role": "system", "content": "You are a helpful AI date planner."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=300
    )

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    prefs = get_user_preferences()
    plan = generate_ai_plan(prefs)
    print("\n💡 Your Personalized Date Plan:\n")
    print(plan)
