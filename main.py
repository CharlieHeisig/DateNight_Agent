# main.py

import openai
from config import OPENAI_API_KEY

def get_user_preferences():
    print("Welcome to DateNight!")
    location = input("Where will your date be?")
    budget = input("What's your budget? ")
    food = input("Any preferred cuisine or dining experience? ")
    vibe = input("Do you want something romantic, fun, adventurous? ")
    activity = input("Any specific activity (movie, hike, museum)? ")
    time = input("Will this be an afternoon, evening, or weekend plan? ")

    return {
        "location": location,
        "budget": budget,
        "food": food,
        "vibe": vibe,
        "activity": activity,
        "time": time
    }

from openai import OpenAI

def generate_ai_plan(preferences):
    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
You are a creative and thoughtful date planning assistant.
Given the user's preferences below, generate a fun, romantic, and personalized date night plan. 
Please include a mix of activities, dining options, and any special touches that would make the date memorable.
Please include a link to a Google Maps location for every location.
Please estimate the driving/walking/etc. time between locations.
Select a variety of activities that suit the user's preferences and budget all within a 15 min transportation time of eacother.
Please estimate the amount of money that will be spent at each location, and create a total budget for the date.

Preferences:
- Location: {preferences['location']}
- Budget: {preferences['budget']}
- Cuisine: {preferences['food']}
- Vibe: {preferences['vibe']}
- Activity: {preferences['activity']}
- Time: {preferences['time']}

Respond with a short 3-step plan, written in a friendly tone.
"""

    response = client.chat.completions.create(
        model="gpt-4",  
        messages=[
            {"role": "system", "content": "You are a helpful AI date planner."},
            {"role": "user", "content": prompt}
        ],
        temperature=1.3,
        max_tokens=1000
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    prefs = get_user_preferences()
    plan = generate_ai_plan(prefs)
    print("\n Your Personalized Date Plan:\n")
    print(plan)
