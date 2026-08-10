import os

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

from prompt import create_travel_prompt


# =========================================================
# LOAD ENVIRONMENT
# =========================================================

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError(
        "OPENROUTER_API_KEY is missing from your .env file."
    )


# =========================================================
# OPENROUTER AI
# =========================================================

llm = ChatOpenRouter(
    model="openrouter/free",
    temperature=0.7,
    max_tokens=3000,
    max_retries=2,
)


# =========================================================
# GENERATE TRAVEL PLAN
# =========================================================

def generate_trip_plan(
    destination,
    days,
    budget,
    people,
    interests
):

    prompt = create_travel_prompt(
        destination=destination,
        days=days,
        budget=budget,
        people=people,
        interests=interests
    )

    response = llm.invoke(prompt)

    return response.content