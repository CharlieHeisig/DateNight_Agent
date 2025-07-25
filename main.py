# main.py
print("✅ main.py is running!")

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

def generate_plan(prefs):
    plan = f"\n🌟 Here's your personalized date night plan in {prefs['location']}:\n"
    plan += f"1. Start with a {prefs['food']} dinner within your {prefs['budget']} budget.\n"
    plan += f"2. Then enjoy a {prefs['activity']} – perfect for a {prefs['vibe']} vibe.\n"
    plan += f"3. Timing: Ideal for a {prefs['time']} outing.\n"
    return plan

if __name__ == "__main__":
    prefs = get_user_preferences()
    plan = generate_plan(prefs)
    print(plan)
