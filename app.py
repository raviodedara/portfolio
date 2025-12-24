import streamlit as st

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Ravio | AI Architect", page_icon="🤖", layout="wide")

# --- 2. THEME & STYLING (Dark + Blue + Red) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* Text Colors */
    .stMarkdown, p, li, label { color: #3399FF !important; font-size: 17px; }
    h1, h2, h3 { color: #66B2FF !important; font-weight: 800 !important; }

    /* The 'Action' Button */
    .view-work-btn {
        background-color: #FF4B4B;
        color: white !important;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 15px;
        transition: 0.3s;
    }
    .view-work-btn:hover { background-color: #ff3333; transform: scale(1.05); }

    /* Clean Section Cards */
    .card {
        background-color: #1a1c24;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 20px;
    }
    
    html { scroll-behavior: smooth; }
    </style>
""", unsafe_allow_html=True)

# --- 3. HERO SECTION (Punchy & Direct) ---
st.markdown('<p style="font-size:65px; font-weight:900; margin-bottom:0px;">RAVI ODEDARA</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:24px; color: #FF4B4B; font-weight:bold;">AI Solution Architect</p>', unsafe_allow_html=True)

col1, _ = st.columns([2, 1])
with col1:
    st.write("I build private, secure AI Agents for businesses. I specialize in the **'Bring Your Own Key'** model to keep your data internal and your costs low.")
    st.markdown('<a href="#work" class="view-work-btn">View My Recent Work</a>', unsafe_allow_html=True)

st.write("#") # Spacer

# --- 4. FEATURED PROJECT (Data Pilot) ---
st.markdown("<div id='work'></div>", unsafe_allow_html=True)
st.write("---")
st.markdown("## ✈️ Featured: Data Pilot AI")

with st.container():
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("""
        <div class="card">
            <h3>The AI Data Analyst</h3>
            <p>A professional tool that cleans, visualizes, and maps data using Natural Language.</p>
            <ul>
                <li><b>Safe-Mode:</b> Instant 'Undo' for data edits.</li>
                <li><b>Private:</b> Runs on your private Gemini API key.</li>
                <li><b>Smart:</b> Auto-detects the best model for your tasks.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Launch Live Demo 🚀", "https://datapilot101.streamlit.app/", use_container_width=True)
    
    with c2:
        # Visual proof: This link shows a professional data icon
        st.image("https://img.icons8.com/clouds/500/data-configuration.png", width=350)

st.write("#")

# --- 5. SERVICES (Grid Layout) ---
st.write("---")
st.markdown("## 🛠️ Specialized Services")
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("### 🤖 Private AI")
    st.write("Tailored LLM agents that live on your private infrastructure.")
with s2:
    st.markdown("### 🧹 Automation")
    st.write("Python pipelines that clean messy data while you sleep.")
with s3:
    st.markdown("### 📈 Visuals")
    st.write("Interactive Plotly/Mapbox dashboards for executives.")

# --- 6. FOOTER ---
st.write("#")
st.write("---")
st.markdown("<center>Ready to automate? <b>your-email@example.com</b></center>", unsafe_allow_html=True)
st.markdown("<center>LinkedIn | GitHub</center>", unsafe_allow_html=True)
