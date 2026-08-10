# ✈️ AI Travel Planner Agent

AI Travel Planner is a simple AI-powered application that creates personalized travel plans based on the user's destination, trip duration, budget, number of travellers, and interests.

## Features

- 📍 Destination-based travel planning
- 🗓️ Day-by-day itinerary generation
- 💰 Budget-aware planning
- 👥 Multiple traveller support
- ❤️ Personalized travel preferences
- 🍴 Food recommendations
- 🚕 Transportation suggestions
- 💡 Practical travel tips
- 📄 Downloadable travel plan

## Technologies Used

- Python
- Streamlit
- LangChain
- OpenRouter AI
- Python-dotenv

## Project Structure

```text
AI_Travel_Planner/
│
├── app.py
├── agent.py
├── prompt.py
├── tools.py
├── requirements.txt
├── .env
└── README.md
How It Works

The user enters trip details and preferences. The AI processes the information and generates a personalized day-by-day travel itinerary with budget, food, transportation, and travel recommendations.

Setup

Install the required packages:

pip install -r requirements.txt

Add your OpenRouter API key to .env:

OPENROUTER_API_KEY=your_api_key_here

Run the application:

streamlit run app.py
Purpose

This project demonstrates the use of AI and agent-based technologies to build a practical travel planning application.

Author

Anubhab Nandi