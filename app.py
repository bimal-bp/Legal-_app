# app.py
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Legalink",
    page_icon="⚖️",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home", "👤 Profile", "⚖️ Attorneys", "🏥 Legal Aid",
    "📅 Proceedings", "📚 Resources", "🔄 Rehabilitation", "🤖 AI Lawbot"
])

# Load pages dynamically
if page == "🏠 Home":
    from pages import 1_🏠_Home
elif page == "👤 Profile":
    from pages import 2_👤_Profile
elif page == "⚖️ Attorneys":
    from pages import 3_⚖️_Attorneys
elif page == "🏥 Legal Aid":
    from pages import 4_🏥_Legal_Aid
elif page == "📅 Proceedings":
    from pages import 5_📅_Proceedings
elif page == "📚 Resources":
    from pages import 6_📚_Resources
elif page == "🔄 Rehabilitation":
    from pages import 7_🔄_Rehabilitation
elif page == "🤖 AI Lawbot":
    from pages import 8_🤖_AI_Lawbot
