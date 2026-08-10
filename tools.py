# =========================================================
# BASIC BUDGET TOOL
# =========================================================

def calculate_basic_budget(
    total_budget,
    days,
    people
):
    """
    Calculate simple daily and per-person budget.
    """

    # Prevent invalid values
    if days <= 0:
        days = 1

    if people <= 0:
        people = 1

    daily_budget = total_budget / days
    person_budget = total_budget / people

    return {
        "daily_budget": round(daily_budget, 2),
        "person_budget": round(person_budget, 2),
        "total_budget": round(total_budget, 2)
    }


# =========================================================
# SIMPLE BUDGET BREAKDOWN
# =========================================================

def estimate_budget(total_budget):
    """
    Create a simple estimated budget distribution.
    """

    accommodation = total_budget * 0.35
    food = total_budget * 0.20
    transportation = total_budget * 0.20
    activities = total_budget * 0.15
    other = total_budget * 0.10

    return {
        "Accommodation": round(accommodation, 2),
        "Food": round(food, 2),
        "Transportation": round(transportation, 2),
        "Activities": round(activities, 2),
        "Other": round(other, 2),
        "Total": round(total_budget, 2)
    }


# =========================================================
# VALIDATE TRIP INPUT
# =========================================================

def validate_trip_input(
    destination,
    days,
    budget,
    people
):
    """
    Validate basic travel information.
    """

    errors = []

    if not destination or not destination.strip():
        errors.append("Destination is required.")

    if days <= 0:
        errors.append("Number of days must be greater than 0.")

    if budget <= 0:
        errors.append("Budget must be greater than 0.")

    if people <= 0:
        errors.append("Number of travellers must be greater than 0.")

    return errors