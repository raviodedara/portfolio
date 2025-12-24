import streamlit as st
import io

# --- 1. PAGE CONFIGURATION ---
# This must be the first Streamlit command
st.set_page_config(
    page_title="Raviodedara | AI Architect",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED STYLING (Dark Theme + Blue Text + Red Buttons) ---
st.markdown("""
    <style>
    /* Global Background and Text Color (Blue) */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Force Blue text for all markdown and paragraphs */
    .stMarkdown, p, li, span, label {
        color: #3399FF !important;
    }
    
    /* Headers in a slightly lighter Blue for visibility */
    h1, h2, h3, h4 {
        color: #66B2FF !important;
        font-weight: 800 !important;
    }

    /* Subheaders and Metrics */
    .stMetric label, .stMetric div {
        color: #66B2FF !important;
    }

    /* Professional Red Button for 'View Work' (Scroll Link) */
    .view-work-btn {
        background-color: #FF4B4B;
        color: white !important;
        padding: 14px 28px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        border: none;
        margin-top: 20px;
        transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3);
    }
    .view-work-btn:hover {
        background-color: #ff3333;
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(255, 75, 75, 0.4);
        color: white !important;
    }

    /* Project Cards / Containers */
    .project-card {
        background-color: #1a1c24;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #3399FF33;
    }

    /* Smooth scroll behavior */
    html {
        scroll-behavior: smooth;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("Navigation")
    st.markdown("---")
    st.info("💡 **Hire Me:** I build custom AI Agents for businesses. Let's automate your data.")
    st.markdown("---")
    st.write("📧 **Contact:** your-email@example.com")
    st.write("🔗 [LinkedIn](#) | [GitHub](#)")

# --- 4. HERO SECTION ---
st.markdown('<p style="font-size:60px; font-weight:900; margin-bottom:0px; line-height:1;">RAVIO DEDARA</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:26px; color: #FF4B4B; font-weight:bold; margin-top:10px;">AI Solution Architect & Data Automator</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    I specialize in building **Private AI Agents** that bridge the gap between complex data and business decisions. 
    By implementing 'Bring Your Own Key' (BYOK) models, I help companies leverage the power of LLMs like Gemini 1.5 
    while keeping their data internal and costs under total control.
    """)
    # The Action Button (Uses the CSS class defined above)
    st.markdown('<a href="#projects" class="view-work-btn">View My Recent Work</a>', unsafe_allow_html=True)

with col2:
    # This acts as a visual spacer or you can put a headshot here
    st.empty()

# --- 5. FEATURED PROJECT: DATA PILOT AI ---
# The Anchor for the scroll button
st.markdown("<div id='projects' style='padding-top: 50px;'></div>", unsafe_allow_html=True)
st.write("---")

st.markdown("## 🚀 Featured Project: Data Pilot AI")
st.markdown("""
<div class="project-card">
    <p style="font-size:18px;">A professional-grade AI Analyst that allows users to clean, visualize, and interact 
    with their data using natural language commands.</p>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("### 👨🏼‍✈️ The Pilot in Action")
    # Replace this link with a screenshot of your actual map/dashboard
    st.image("https://img.icons8.com/clouds/500/data-configuration.png", use_container_width=True)
    st.write("**Tech Stack:** Python, Streamlit, Google Gemini 1.5, Pandas, Plotly Express.")

with c2:
    st.markdown("### 🛠️ Key Technical Solves")
    st.write("""
    - **Safe-Mode Architecture:** Created an immutable 'Original Data' backup system allowing users to 'Undo' any AI-driven data modification.
    - **Session State Persistence:** Engineered complex memory handling to ensure user API keys and chat history survive page reruns.
    - **Automated Data Cleaning:** Trained the agent to distinguish between 'View' commands (Show me) and 'Action' commands (Delete rows).
    - **Private Mapping:** Implemented Mapbox-free geospatial visualization using OpenStreetMap tiles.
    """)
    st.link_button("Launch Live Demo ✈️", "https://datapilot101.streamlit.app/", use_container_width=True)

# --- 6. SERVICES & EXPERTISE ---
st.write("---")
st.markdown("## 🛠️ Specialized Services")

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("### 🤖 Custom AI Agents")
    st.write("Design and deployment of tailored LLM agents that live on your private infrastructure.")

with s2:
    st.markdown("### 🧹 Data Engineering")
    st.write("Building automated Python scripts to clean, transform, and merge fragmented business datasets.")

with s3:
    st.markdown("### 📈 Visual Intelligence")
    st.write("Developing interactive, real-time dashboards for executives to monitor KPIs instantly.")

# --- 7. CONTACT / FOOTER ---
st.write("---")
st.markdown("<center><p style='color: #66B2FF;'>Interested in a custom build or freelance collaboration?</p></center>", unsafe_allow_html=True)
st.markdown("<center><p style='font-size:20px; font-weight:bold;'>Let's connect: <u>your-email@example.com</u></p></center>", unsafe_allow_html=True)
