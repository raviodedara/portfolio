import streamlit as st

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Raviodedara | AI Architect", page_icon="🤖", layout="wide")

# --- 2. DARK MODE STYLING ---
st.markdown("""
    <style>
    /* Ensure the main background is dark */
    .stApp {
        background-color: #0e1117;
    }
    /* Style the scrollable button to be visible and attractive */
    .view-work-btn {
        background-color: #FF4B4B;
        color: white;
        padding: 12px 24px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        border: none;
    }
    .view-work-btn:hover {
        background-color: #ff3333;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HERO SECTION ---
st.markdown('<p style="font-size:50px; font-weight:900;">RAVIO DEDARA</p>', unsafe_allow_html=True)

# FIX for the "View My Recent Work" Button
st.markdown('<a href="#projects" class="view-work-btn">View My Recent Work</a>', unsafe_allow_html=True)

# ... (Continue with the rest of your portfolio sections)
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.header("🚀 Featured Project: Data Pilot AI")
