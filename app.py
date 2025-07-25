# app.py

import streamlit as st
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="datenight. | AI Date Planner", layout="centered")
st.title("💜 datenight. – AI Date Planner")

st.markdown("Fill in your preferences and let AI craft the perfect night.")

with st.form("date_form"):
    location = st.text_input("📍 Location")
    budget = st.selectbox("💸 Budget", ["$", "$$", "$$$"])
    food = st.text_input("🍽️ Cuisine or Dining Preference")
    vibe = st.text_input("💜 Vibe (romantic, fun, adventurous...)")
    activity = st.text_input("🎭 Activity (e.g., movie, hike, museum)")
    time = st.selectbox("🕒 Time of Day", ["Evening", "Afternoon", "Weekend"])

    submitted = st.form_submit_button("Generate My Date Plan 💡")

if submitted:
    with st.spinner("Planning your night..."):

        prompt = f"""
You are a creative and thoughtful AI assistant helping someone plan a special date night.

Here are the user’s preferences:
- Location: {location}
- Budget: {budget}
- Cuisine: {food}
- Vibe: {vibe}
- Activity: {activity}
- Time: {time}

Create a 3-part date night plan tailored to them, using a fun and friendly tone.
"""

        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful and imaginative date planner."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=300
        )

        plan = response.choices[0].message.content
        st.markdown("### 💡 Your Personalized Date Plan:")
        st.success(plan)
