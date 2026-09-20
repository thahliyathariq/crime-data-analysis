# ==========================================================
# PROFESSIONAL UI DESIGN
# ==========================================================

import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Crime Intelligence Dashboard",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="collapsed"
)
#first old

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* ================= GENERAL ================= */

.stApp {
    background-color: #0f172a;
    color: #e5e7eb;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}


/* ================= HEADER ================= */

.main-title {
    font-size: 34px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 2px;
}

.subtitle {
    font-size: 15px;
    color: #94a3b8;
    margin-bottom: 25px;
}


/* ================= SECTION HEADERS ================= */

.section-title {
    font-size: 22px;
    font-weight: 650;
    color: #f1f5f9;
    margin-top: 25px;
    margin-bottom: 12px;
    border-left: 4px solid #38bdf8;
    padding-left: 12px;
}


/* ================= CARDS ================= */

.dashboard-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.20);
}

.card-title {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 7px;
}

.card-value {
    color: #f8fafc;
    font-size: 27px;
    font-weight: 700;
}

.card-description {
    color: #64748b;
    font-size: 12px;
    margin-top: 5px;
}


/* ================= METRICS ================= */

[data-testid="stMetric"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 18px;
    border-radius: 14px;
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

[data-testid="stMetricValue"] {
    color: #f8fafc !important;
}


/* ================= BUTTONS ================= */

.stButton > button {
    border-radius: 9px;
    border: 1px solid #334155;
    background-color: #1e293b;
    color: #f8fafc;
    font-weight: 600;
    padding: 8px 18px;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #38bdf8;
    color: #38bdf8;
}


/* ================= PRIMARY BUTTON ================= */

.stButton > button[kind="primary"] {
    background-color: #0284c7;
    color: white;
    border: none;
}

.stButton > button[kind="primary"]:hover {
    background-color: #0369a1;
    color: white;
}


/* ================= INPUT BOXES ================= */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div,
.stMultiSelect div {
    border-radius: 9px !important;
}


/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #334155;
}


/* ================= EXPANDERS ================= */

.streamlit-expanderHeader {
    background-color: #1e293b;
    border-radius: 10px;
}


/* ================= DATAFRAME ================= */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}


/* ================= DIVIDER ================= */

hr {
    border-color: #334155;
}


/* ================= ALERT BOXES ================= */

.stAlert {
    border-radius: 10px;
}


/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding-top: 35px;
    padding-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


















#old
import requests


import streamlit as st
import pandas as pd
from datetime import datetime
import os


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Crime Data Analysis",
    page_icon="🚨",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚨 Crime Data Analysis")
st.header("WELCOME")
st.write("Welcome to the Crime Data Analysis Dashboard.")



# --------------------------------------------------
# TOP RIGHT MENU
# --------------------------------------------------

col1, col2 = st.columns([10, 1])

with col2:

    menu = st.popover("☰")

    with menu:

        st.write("### Menu")

        complaint_button = st.button(
            "🚨 Complaint Corner",
            use_container_width=True
        )

        feedback_button = st.button(
            "⭐ Service Feedback Corner",
            use_container_width=True
        )

        update_button = st.button(
            "🔄 Update on Existing Data / Service",
            use_container_width=True
        )


# --------------------------------------------------
# PAGE SELECTION
# --------------------------------------------------

if "menu_page" not in st.session_state:

    st.session_state.menu_page = "home"


if complaint_button:

    st.session_state.menu_page = "complaint"


if feedback_button:

    st.session_state.menu_page = "feedback"


if update_button:

    st.session_state.menu_page = "update"


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------



    st.info(
        "Use the ☰ menu in the top-right corner "
        "to submit a complaint, provide feedback, "
        "or suggest an update."
    )


# --------------------------------------------------
# COMPLAINT CORNER
# --------------------------------------------------

elif st.session_state.menu_page == "complaint":

    st.header("🚨 Complaint Corner")

    st.write(
        "Report a nuisance, safety concern, "
        "or other threat."
    )

    st.divider()

    # First question
    st.subheader("1. Who are you?")

    user_category = st.radio(
        "Please select an option:",
        [
            "Woman",
            "Solo Traveler",
            "Man",
            "Other / Prefer not to say"
        ]
    )


    # Second question
    st.subheader("2. What kind of threat are you facing?")

    threat_type = st.selectbox(
        "Select the type of threat:",
        [
            "Harassment",
            "Suspicious activity",
            "Unsafe location",
            "Theft",
            "Verbal threat",
            "Physical safety concern",
            "Nuisance",
            "Other"
        ]
    )


    # Complaint box
    st.subheader("3. Describe the problem")

    complaint = st.text_area(
        "Please enter your complaint:",
        placeholder="Describe what happened or what safety issue you noticed...",
        height=180
    )


    # Submit button
    if st.button(
        "🚨 Submit Complaint",
        type="primary"
    ):

        if complaint.strip() == "":

            st.warning(
                "Please enter your complaint before submitting."
            )

        else:

            complaint_data = pd.DataFrame({
                "Date & Time": [
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ],
                "User Category": [
                    user_category
                ],
                "Threat Type": [
                    threat_type
                ],
                "Complaint": [
                    complaint
                ]
            })


            # Save complaint
            file_name = "complaints.csv"

            if os.path.exists(file_name):

                complaint_data.to_csv(
                    file_name,
                    mode="a",
                    header=False,
                    index=False
                )

            else:

                complaint_data.to_csv(
                    file_name,
                    index=False
                )


            st.success(
                "✅ Your complaint has been recorded."
            )

            st.info(
                "Complaint ID: CR-"
                + datetime.now().strftime("%Y%m%d%H%M%S")
            )


# --------------------------------------------------
# SERVICE FEEDBACK
# --------------------------------------------------

elif st.session_state.menu_page == "feedback":

    st.header("⭐ Service Feedback Corner")

    st.write(
        "Please enter your feedback about the "
        "service provided."
    )

    st.divider()


    feedback = st.text_area(
        "Please enter your feedback:",
        placeholder="Tell us about your experience...",
        height=200
    )


    rating = st.slider(
        "How would you rate the service?",
        1,
        5,
        3
    )


    if st.button(
        "⭐ Submit Feedback",
        type="primary"
    ):

        if feedback.strip() == "":

            st.warning(
                "Please enter your feedback."
            )

        else:

            feedback_data = pd.DataFrame({
                "Date & Time": [
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ],
                "Rating": [
                    rating
                ],
                "Feedback": [
                    feedback
                ]
            })


            file_name = "service_feedback.csv"


            if os.path.exists(file_name):

                feedback_data.to_csv(
                    file_name,
                    mode="a",
                    header=False,
                    index=False
                )

            else:

                feedback_data.to_csv(
                    file_name,
                    index=False
                )


            st.success(
                "✅ Thank you! Your feedback has been recorded."
            )


# --------------------------------------------------
# UPDATE EXISTING DATA / SERVICE
# --------------------------------------------------

elif st.session_state.menu_page == "update":

    st.header("🔄 Update on Existing Data / Service")

    st.write(
        "Please tell us about any information or "
        "service that needs to be updated."
    )

    st.divider()


    update = st.text_area(
        "Enter the update or correction:",
        placeholder="Example: A location is incorrectly marked as unsafe...",
        height=200
    )


    if st.button(
        "🔄 Submit Update",
        type="primary"
    ):

        if update.strip() == "":

            st.warning(
                "Please enter the update before submitting."
            )

        else:

            update_data = pd.DataFrame({
                "Date & Time": [
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ],
                "Update": [
                    update
                ]
            })


            file_name = "data_updates.csv"


            if os.path.exists(file_name):

                update_data.to_csv(
                    file_name,
                    mode="a",
                    header=False,
                    index=False
                )

            else:

                update_data.to_csv(
                    file_name,
                    index=False
                )


            st.success(
                "✅ Thank you! Your update has been recorded."
            )
















import streamlit as st
import pandas as pd
 

st.slider("Select year", 2001, 2026)

st.selectbox(
    "Select crime type",
    ["THEFT", "MURDER", "BATTERY","ASSAULT"]
)

st.button("Analyze",key="analyze_button")

import streamlit as st
from src.data_loader import load_crime_data


st.set_page_config(
    page_title="Crime Data Analysis",
    page_icon="🚨",
    layout="wide"
)


st.title(" Crime Data Analysis Dashboard")

st.write(
    "Interactive analysis of publicly available crime data."
)


with st.spinner("Loading crime data..."):

    df = load_crime_data(50000)


st.success("Crime data loaded successfully!")



import streamlit as st
from urllib.parse import quote

# ---------------- EMERGENCY HELP ----------------

@st.dialog("🚨 Do you need urgent help?")
def emergency_popup():

    st.warning("If you are in immediate danger, contact emergency services.")

    location = st.selectbox(
        "📍 Select your location",
        ["chicago", "Other State"]
    )

    if location == "chicago":

        st.subheader("☎️ Emergency Contacts")

        st.info("🚨 Emergency: **911**")
        st.info("💻 Cyber Crime: **311**")
        st.info("👩 Women Helpline: **112**")
        st.info("👶 Child Helpline: * 312-492-3810***")

        st.divider()

        st.subheader("📍 Find Nearby Help")

        # Google Maps searches
        police_url = (
            "https://www.google.com/maps/search/?api=1&query="
            + quote("police station near me")
        )

        public_url = (
            "https://www.google.com/maps/search/?api=1&query="
            + quote("public place near me")
        )

        hospital_url = (
            "https://www.google.com/maps/search/?api=1&query="
            + quote("hospital near me")
        )

        st.link_button("👮 Find Nearest Police Station", police_url)

        st.link_button("🏙️ Find Nearby Public Places", public_url)

        st.link_button("🏥 Find Nearby Hospital", hospital_url)

        st.divider()

        st.subheader("🛡️ Safety Tips")

        st.write("• Move to a safe and populated place if possible.")
        st.write("• Contact a trusted person.")
        st.write("• Avoid sharing your personal information with strangers.")
        st.write("• If there is immediate danger, contact emergency services.")

    else:

        st.info(
            "For other Indian states, select your state in the future "
            "to display verified local emergency contacts."
        )


# Button shown on the main dashboard
if st.button("🚨 Do you need urgent help?", use_container_width=True):
    emergency_popup()


st.subheader("Dataset Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "Crime Categories",
    df["primary_type"].nunique()
)

col3.metric(
    "Locations",
    df["location_description"].nunique()
)
st.subheader("Most Common Crime Types")

crime_counts = (
    df["primary_type"]
    .value_counts()
    .head(10)
)

st.bar_chart(crime_counts)

st.subheader("Crime by Location")

location_counts = (
    df["location_description"]
    .value_counts()
    .head(10)
)

st.bar_chart(location_counts)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)
df["year"] = df["date"].dt.year

df["hour"] = df["date"].dt.hour

hour_counts = (
    df["hour"]
    .value_counts()
    .sort_index()
)

st.subheader("Crime by Hour")

st.line_chart(hour_counts)
import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium


import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
st.header("🔥 Crime Hotspot Analysis")

if "latitude" in df.columns and "longitude" in df.columns:

    heat_df = df[["latitude", "longitude"]].copy()

    heat_df["latitude"] = pd.to_numeric(heat_df["latitude"], errors="coerce")
    heat_df["longitude"] = pd.to_numeric(heat_df["longitude"], errors="coerce")

    heat_df = heat_df.dropna()

    st.write("Number of locations:", len(heat_df))

    if len(heat_df) > 0:

        m = folium.Map(
            location=[
                heat_df["latitude"].mean(),
                heat_df["longitude"].mean()
            ],
            zoom_start=10
        )

        heat_data = heat_df[["latitude", "longitude"]].values.tolist()

        HeatMap(
            heat_data,
            radius=20,
            blur=25,
            min_opacity=0.4
        ).add_to(m)

        st_folium(m, width=900, height=600)

    else:
        st.warning("No valid latitude and longitude data found.")

else:
    st.warning("Latitude and Longitude columns are missing")









    
@st.cache_data(ttl=600)
def load_crime_data(limit=50000):

    url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

    params = {
        "$limit": limit,
        "$order": "date DESC"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return pd.DataFrame(response.json())


#location monitor02

# ============================================================
# 📍 LOCATION-BASED SAFETY ALERT
# ============================================================

import streamlit as st
import math
import pandas as pd


# ------------------------------------------------------------
# 1. CALCULATE DISTANCE BETWEEN TWO LOCATIONS
# ------------------------------------------------------------

def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius in km

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return R * c


# ------------------------------------------------------------
# 2. LOCATION SAFETY MONITOR
# ------------------------------------------------------------

st.markdown(
    '<div class="section-title">📍 Location Safety Monitor</div>',
    unsafe_allow_html=True
)

st.write(
    "Check whether your current location is near an area "
    "with a higher concentration of reported crime."
)


# ------------------------------------------------------------
# 3. MANUAL LOCATION
# ------------------------------------------------------------

with st.expander("📌 Enter location manually"):

    col1, col2 = st.columns(2)

    with col1:
        manual_lat = st.number_input(
            "Latitude",
            value=41.8788,
            format="%.6f"
        )

    with col2:
        manual_lon = st.number_input(
            "Longitude",
            value=-87.7305,
            format="%.6f"
        )

    use_manual = st.checkbox(
        "Use this location"
    )


# ------------------------------------------------------------
# 4. BROWSER LOCATION
# ------------------------------------------------------------

location_data = None

try:

    from streamlit_js_eval import get_geolocation

    if not use_manual:
        location_data = get_geolocation()

except Exception:

    location_data = None


# ------------------------------------------------------------
# 5. GET USER COORDINATES
# ------------------------------------------------------------

user_lat = None
user_lon = None

if use_manual:

    user_lat = manual_lat
    user_lon = manual_lon

elif location_data:

    if "coords" in location_data:

        user_lat = location_data["coords"].get(
            "latitude"
        )

        user_lon = location_data["coords"].get(
            "longitude"
        )


# ------------------------------------------------------------
# 6. REAL POPUP DIALOG
# ------------------------------------------------------------

@st.dialog(
    "🚨 Location Safety Alert",
    dismissible=True
)
def show_safety_alert(nearby_count):

    st.error(
        "⚠️ Be careful, your location is not safe"
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#888888;
            margin-top:-12px;
            margin-bottom:15px;
        ">
            Conclusion drawn from the available dataset
        </div>
        """,
        unsafe_allow_html=True
    )

    st.metric(
        "Reported Crime Records",
        f"{nearby_count:,}"
    )

    st.caption(
        "More than 10 reported crime records were found "
        "within 2 km of your location."
    )

    st.info(
        "This warning is based on reported crime records "
        "available in the dataset. It does not by itself "
        "determine that a location is actually unsafe."
    )


# ------------------------------------------------------------
# 7. CHECK LOCATION
# ------------------------------------------------------------

if user_lat is not None and user_lon is not None:

    st.success(
        f"📍 Location detected: "
        f"{user_lat:.5f}, {user_lon:.5f}"
    )


    # --------------------------------------------------------
    # CHICAGO CRIME API DATA
    # IMPORTANT:
    # Uses df, NOT filtered_df
    # --------------------------------------------------------

    required_columns = [
        "latitude",
        "longitude"
    ]


    if all(
        column in df.columns
        for column in required_columns
    ):

        location_df = df.copy()


        # Convert coordinates to numbers

        location_df["latitude"] = pd.to_numeric(
            location_df["latitude"],
            errors="coerce"
        )

        location_df["longitude"] = pd.to_numeric(
            location_df["longitude"],
            errors="coerce"
        )


        # Remove records without coordinates

        location_df = location_df.dropna(
            subset=[
                "latitude",
                "longitude"
            ]
        )


        # ----------------------------------------------------
        # SEARCH RADIUS
        # ----------------------------------------------------

        SEARCH_RADIUS_KM = 2.0

        nearby_crimes = []


        for _, row in location_df.iterrows():

            distance = calculate_distance(
                user_lat,
                user_lon,
                row["latitude"],
                row["longitude"]
            )

            if distance <= SEARCH_RADIUS_KM:

                nearby_crimes.append(
                    distance
                )


        nearby_count = len(
            nearby_crimes
        )


        # ----------------------------------------------------
        # ALERT THRESHOLD
        # More than 10 records
        # ----------------------------------------------------

        HIGH_CRIME_THRESHOLD = 10


        # ----------------------------------------------------
        # AUTOMATIC POPUP
        # ----------------------------------------------------

        if nearby_count > HIGH_CRIME_THRESHOLD:

            if (
                "safety_alert_shown"
                not in st.session_state
            ):

                st.session_state.safety_alert_shown = False


            if not st.session_state.safety_alert_shown:

                st.session_state.safety_alert_shown = True

                show_safety_alert(
                    nearby_count
                )


        # ----------------------------------------------------
        # NORMAL STATUS
        # ----------------------------------------------------

        if nearby_count <= HIGH_CRIME_THRESHOLD:

            st.markdown(
                f"""
                <div style="
                    padding:18px;
                    margin:15px 0 25px 0;
                    background:#172554;
                    border:1px solid #334155;
                    border-radius:15px;
                    color:#e2e8f0;
                ">

                    <div style="
                        font-size:20px;
                        font-weight:700;
                    ">
                        📊 Crime Records Nearby
                    </div>

                    <div style="
                        margin-top:8px;
                    ">
                        {nearby_count:,}
                        reported records were found
                        within {SEARCH_RADIUS_KM} km.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


    else:

        st.warning(
            "Latitude and Longitude data are not available "
            "in the Chicago Crime API dataset."
        )


else:

    st.info(
        "📍 Location permission was not available. "
        "Allow location access in your browser or use "
        "the manual location option above."
    )