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
    from home import home_page
    home_page()
elif page == "👤 Profile":
    from profile import profile_page
    profile_page()
elif page == "⚖️ Attorneys":
    from attorneys import attorneys_page
    attorneys_page()
elif page == "🏥 Legal Aid":
    from legal_aid import legal_aid_page
    legal_aid_page()
elif page == "📅 Proceedings":
    from proceedings import proceedings_page
    proceedings_page()
elif page == "📚 Resources":
    from resources import resources_page
    resources_page()
elif page == "🔄 Rehabilitation":
    from rehabilitation import rehabilitation_page
    rehabilitation_page()
elif page == "🤖 AI Lawbot":
    from lawbot import lawbot_page
    lawbot_page()
