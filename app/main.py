"""Streamlit entrypoint for AIxplore."""
import sys
from pathlib import Path

import streamlit as st


# Ensure repository root is on sys.path so `app.*` imports resolve when run via streamlit
ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
PARENT_STR = str(PARENT)
if PARENT_STR not in sys.path:
    sys.path.insert(0, PARENT_STR)  # prioritize local app package over site-packages

from app.pages import login, home, itinerary, upload

st.set_page_config(page_title="AIXplore", layout="wide")

# Initialize selected page state
if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Home"

def navigate(page):
    st.session_state["selected_page"] = page

# Display navigation as blocks/cards
st.markdown("##  AIXplore Navigation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button(" Login", use_container_width=True):
        navigate("Login")

with col2:
    if st.button(" Home", use_container_width=True):
        navigate("Home")

with col3:
    if st.button("Itinerary", use_container_width=True):
        navigate("Itinerary")

with col4:
    if st.button(" Upload Photo", use_container_width=True):
        navigate("Upload")

st.write("---")  # Divider

# Load the selected page
page = st.session_state["selected_page"]

if page == "Login":
    login.show()
elif page == "Home":
    home.show()
elif page == "Itinerary":
    itinerary.show()
elif page == "Upload":
    upload.show()
