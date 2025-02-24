# pages/1_🏠_Home.py
import streamlit as st

st.title("🏠 Home")
st.write("Welcome to Legalink! Your one-stop solution for legal assistance.")

# Trial Management
st.subheader("Trial Management")
st.write("View your current and past trials here.")

# Quick Access
st.subheader("Quick Access")
col1, col2, col3 = st.columns(3)
with col1:
    st.button("👤 Profile")
with col2:
    st.button("⚖️ Attorneys")
with col3:
    st.button("🏥 Legal Aid")
