import streamlit as st

from agent import generate_trip_plan
from tools import calculate_basic_budget


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================
       MAIN APP
    ============================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(75, 100, 255, 0.12),
                transparent 32%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(150, 80, 255, 0.10),
                transparent 30%
            ),
            #080b12;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ==============================
       HERO
    ============================== */

    .hero-icon {
        text-align: center;
        font-size: 48px;
        line-height: 1.5;
        height: 72px;
        padding-top: 5px;
        margin-bottom: 5px;
    }

    .hero-title {
        text-align: center;
        font-size: 44px;
        font-weight: 750;
        letter-spacing: -1.5px;
        color: #ffffff;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        text-align: center;
        color: #9ca5b5;
        font-size: 17px;
        margin-bottom: 35px;
    }


    /* ==============================
       SECTION HEADERS
    ============================== */

    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 20px;
        margin-bottom: 18px;
    }


    /* ==============================
       INPUT AREA
    ============================== */

    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input {
        background-color: rgba(255,255,255,0.06);
        color: #ffffff;
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 14px;
    }

    [data-testid="stTextInput"] input:focus,
    [data-testid="stNumberInput"] input:focus {
        border-color: rgba(255,255,255,0.35);
    }

    label {
        color: #e3e7ee !important;
        font-weight: 600 !important;
    }


    /* ==============================
       MULTISELECT
    ============================== */

    [data-baseweb="select"] > div {
        background-color: rgba(255,255,255,0.06);
        border-radius: 14px;
        border-color: rgba(255,255,255,0.10);
    }


    /* ==============================
       BUTTON
    ============================== */

    .stButton > button {
        width: 100%;
        min-height: 54px;

        border-radius: 16px;

        border: 1px solid rgba(255,255,255,0.12);

        background: linear-gradient(
            135deg,
            #ffffff,
            #dfe5ef
        );

        color: #080b12;

        font-size: 17px;
        font-weight: 750;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 12px 30px rgba(255,255,255,0.12);
    }


    /* ==============================
       METRICS
    ============================== */

    [data-testid="stMetric"] {
        background: rgba(255,255,255,0.045);

        border:
            1px solid rgba(255,255,255,0.08);

        border-radius: 18px;

        padding: 18px;

        box-shadow:
            0 10px 30px rgba(0,0,0,0.15);
    }

    [data-testid="stMetricLabel"] {
        color: #9ca5b5 !important;
    }

    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }


    /* ==============================
       RESULT AREA
    ============================== */

    .result-title {
        font-size: 28px;
        font-weight: 750;
        color: #ffffff;
        margin-top: 35px;
        margin-bottom: 15px;
    }


    /* ==============================
       DIVIDER
    ============================== */

    hr {
        border-color: rgba(255,255,255,0.08);
    }


    /* ==============================
       FOOTER
    ============================== */

    .footer {
        text-align: center;
        color: #626b7a;
        font-size: 13px;
        margin-top: 45px;
        padding-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="hero-icon">✈</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">AI Travel Planner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Your intelligent companion for smarter, easier trips.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# TRIP PLANNING
# =========================================================

st.markdown(
    '<div class="section-title">🌍 Plan your journey</div>',
    unsafe_allow_html=True
)


# =========================================================
# DESTINATION
# =========================================================

destination = st.text_input(
    "📍 Where do you want to go?",
    placeholder="Example: Goa, Darjeeling, Delhi...",
    key="trip_destination"
)


# =========================================================
# BASIC TRIP DETAILS
# =========================================================

col1, col2, col3 = st.columns(3)


with col1:

    days = st.number_input(
        "🗓️ Duration",
        min_value=1,
        max_value=30,
        value=3,
        step=1,
        key="trip_duration"
    )


with col2:

    budget = st.number_input(
        "💰 Total Budget (₹)",
        min_value=1000,
        max_value=1000000,
        value=10000,
        step=500,
        key="trip_budget"
    )


with col3:

    people = st.number_input(
        "👥 Travellers",
        min_value=1,
        max_value=20,
        value=2,
        step=1,
        key="trip_travellers"
    )


# =========================================================
# TRAVEL INTERESTS
# =========================================================

interests = st.multiselect(
    "❤️ What kind of experience do you want?",
    [
        "🏖️ Beaches",
        "🌲 Nature",
        "🏛️ Historical Places",
        "🍴 Food",
        "🛍️ Shopping",
        "🏔️ Adventure",
        "📸 Photography",
        "🌃 Nightlife",
        "🎭 Culture",
        "🧘 Relaxation"
    ],
    default=[
        "🌲 Nature",
        "🍴 Food"
    ],
    key="trip_interests"
)


# =========================================================
# BUDGET CALCULATION
# =========================================================

budget_info = calculate_basic_budget(
    budget,
    days,
    people
)


# =========================================================
# BUDGET OVERVIEW
# =========================================================


# =========================================================
# SPACING
# =========================================================

st.write("")


# =========================================================
# GENERATE BUTTON
# =========================================================

generate = st.button(
    "✨ Create My Travel Plan",
    key="generate_trip_plan",
    use_container_width=True
)


# =========================================================
# GENERATE TRAVEL PLAN
# =========================================================

if generate:

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not destination.strip():

        st.warning(
            "📍 Please enter a destination first."
        )

        st.stop()


    if not interests:

        st.warning(
            "❤️ Please select at least one travel preference."
        )

        st.stop()


    # -----------------------------------------------------
    # AI PROCESS
    # -----------------------------------------------------

    try:

        with st.status(
            "🤖 AI is planning your trip...",
            expanded=True
        ):

            st.write(
                "📍 Understanding your destination..."
            )

            st.write(
                "💰 Checking your budget requirements..."
            )

            st.write(
                "🗓️ Building your day-by-day itinerary..."
            )

            st.write(
                "✨ Personalizing your recommendations..."
            )

            plan = generate_trip_plan(
                destination=destination,
                days=days,
                budget=budget,
                people=people,
                interests=interests
            )


        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

        st.success(
            "🎉 Your personalized travel plan is ready!"
        )


        st.markdown(
            '<div class="result-title">'
            '🗺️ Your Personalized Itinerary'
            '</div>',
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # AI RESULT
        # -------------------------------------------------

        st.markdown(plan)


        # -------------------------------------------------
        # DOWNLOAD TEXT OPTION
        # -------------------------------------------------

        st.download_button(
            label="📄 Download Travel Plan",
            data=plan,
            file_name=f"{destination.replace(' ', '_')}_travel_plan.txt",
            mime="text/plain",
            key="download_trip_plan",
            use_container_width=True
        )


    # -----------------------------------------------------
    # ERROR HANDLING
    # -----------------------------------------------------

    except Exception as error:

        st.error(
            "❌ Unable to generate the travel plan."
        )

        st.warning(
            "Please check your OpenRouter API key and model "
            "configuration."
        )

        with st.expander("Show technical error"):

            st.code(
                str(error)
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    '✈️ AI Travel Planner • Powered by OpenRouter AI'
    '</div>',
    unsafe_allow_html=True
)