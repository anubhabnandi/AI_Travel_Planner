def create_travel_prompt(
    destination,
    days,
    budget,
    people,
    interests
):
    interests_text = ", ".join(interests)

    day_sections = ""

    for day in range(1, days + 1):
        day_sections += f"""

## 🗓️ Day {day}

### 🌅 Morning
Describe suitable morning activities.

### ☀️ Afternoon
Describe suitable afternoon activities.

### 🌆 Evening
Describe suitable evening activities.

### 🍴 Food
Suggest suitable local food or restaurants/food areas.

### 🚕 Transportation
Suggest practical transportation.

### 💰 Estimated Cost
Give an approximate cost for this day.

"""

    prompt = f"""
You are an expert AI Travel Planner.

Create a practical, realistic and enjoyable travel itinerary.

========================
TRIP DETAILS
========================

Destination: {destination}
Duration: {days} days
Travellers: {people}
Total Budget: ₹{budget}
Interests: {interests_text}


========================
INSTRUCTIONS
========================

Create a complete {days}-day itinerary.

{day_sections}

========================
BUDGET
========================

After the daily itinerary, provide:

## 💰 Budget Estimate

- Accommodation
- Food
- Transportation
- Activities
- Other expenses
- Estimated Total

Keep the total reasonably close to ₹{budget}.

Prices are estimates only.


========================
ADDITIONAL SECTIONS
========================

## 🍴 Food Recommendations

Give useful local food suggestions.

## 🚕 Transportation Tips

Give practical transportation advice.

## 💡 Travel Tips

Give useful tips for the destination.

## ⚠️ Important Note

Mention that prices, availability and conditions can change
and should be verified before booking.


========================
RULES
========================

- Prioritize the user's interests.
- Group nearby attractions together.
- Avoid unnecessary travel.
- Prefer affordable options.
- Do not claim live weather.
- Do not claim live hotel availability.
- Do not invent bookings.
- Keep the answer clear and practical.
"""

    return prompt