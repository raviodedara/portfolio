import streamlit as st

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Raviodedara | AI Architect", page_icon="🤖", layout="wide")

# --- 2. HERO SECTION ---
st.markdown('<p style="font-size:45px; font-weight:bold;">Building the Future of Private AI Agents</p>', unsafe_allow_html=True)
st.subheader("I help businesses automate data workflows with custom, secure AI solutions.")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    Most companies are afraid to put their data into public AI tools. 
    I solve that by building **Custom AI Agents** that:
    - 🔒 **Stay Private:** Your data never leaves your environment.
    - 🔑 **Bring Your Own Key:** You control the costs and the API permissions.
    - ⚡ **Automate Everything:** From messy CSV cleaning to complex mapping.
    """)
    st.button("View My Recent Work")

# --- 3. FEATURED PROJECT: DATA PILOT ---
st.write("---")
st.header("🚀 Featured Project: Data Pilot AI")
c1, c2 = st.columns([1, 1])

with c1:
    # Use a screenshot or a GIF of your Data Pilot app here
    st.image("https://via.placeholder.com/600x400.png?text=Data+Pilot+Demo+Video", caption="Data Pilot in Action")

with c2:
    st.write("### The Problem")
    st.write("Data analysts spend 80% of their time 'janitoring' data—cleaning CSVs and fixing types.")
    st.write("### The Solution")
    st.write("""
    I built **Data Pilot**, an AI agent that allows anyone to clean, visualize, and map data using natural language. 
    It features a 'Safe-Mode' backup and a 'Notebook' style interaction for professional precision.
    """)
    st.link_button("Try the Live Demo", "https://datapilot101.streamlit.app/")

# --- 4. SERVICES ---
st.write("---")
st.header("🛠️ How I Can Help Your Business")
s1, s2, s3 = st.columns(3)

with s1:
    st.write("### Custom AI Agents")
    st.write("Tailored AI 'Brains' designed for your specific industry data (Real Estate, E-commerce, Finance).")

with s2:
    st.write("### Data Pipelines")
    st.write("Automating the flow of data from messy spreadsheets into clean, usable dashboards.")

with s3:
    st.write("### AI Strategy")
    st.write("Consulting on how to implement 'Bring Your Own Key' (BYOK) models to save 90% on SaaS fees.")

# --- 5. CONTACT ---
st.write("---")
st.header("📫 Let's Build Something")
st.write("Have a project in mind? Let's talk about how an AI Agent can save you 20+ hours a week.")
st.write("Email: **your-email@example.com**")
