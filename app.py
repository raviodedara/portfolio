import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ravi Odedara | Data Analyst & AI Solutions",
    page_icon="RO",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THE ULTIMATE CSS (Forces Button Colors & Form Styling) ---
st.markdown("""
    <style>
    :root {
        --primary-color: #006666; 
        --accent-color: #FF4B4B;
        --bg-color: #F8F9FA;
    }

    /* Global Background */
    .stApp { background-color: var(--bg-color); }

    /* --- NUCLEAR BUTTON FIX --- */
    /* Target Link Buttons (Live Demo, Source Code, etc.) */
    [data-testid="stLinkButton"] {
        background-color: var(--primary-color) !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        transition: 0.3s !important;
    }
    
    /* Force Link Button Text to be White */
    [data-testid="stLinkButton"] p {
        color: white !important;
        font-weight: bold !important;
    }

    /* Target Regular/Form Buttons (Send Message) */
    [data-testid="baseButton-secondary"], [data-testid="baseButton-primary"] {
        background-color: var(--primary-color) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
    }

    /* Hover effects for all */
    [data-testid="stLinkButton"]:hover, button:hover {
        background-color: #004d4d !important;
        transform: translateY(-2px);
    }

    /* --- NAVIGATION --- */
    .navbar {
        position: fixed; top: 0; left: 0; width: 100%; background: white;
        padding: 15px 50px; z-index: 999; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        display: flex; justify-content: space-between; align-items: center;
    }
    .navbar a { text-decoration: none; color: #333; font-weight: 600; margin-left: 25px; }
    .nav-logo { font-size: 1.5rem; font-weight: 900; color: var(--primary-color) !important; }
    .nav-spacer { height: 80px; }

    /* --- HERO --- */
    .hero-btn-primary {
        background-color: var(--accent-color); color: white !important;
        padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold;
    }
    .hero-btn-secondary {
        background-color: transparent; color: var(--primary-color) !important;
        border: 2px solid var(--primary-color); padding: 10px 22px; border-radius: 8px; font-weight: bold;
    }

    /* --- PROJECT CARDS --- */
    .project-card {
        background-color: white; padding: 25px; border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid var(--primary-color);
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. NAVIGATION ---
st.markdown("""
    <div class="navbar">
        <div class="nav-logo">RO</div>
        <div>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    <div class="nav-spacer"></div>
""", unsafe_allow_html=True)

# --- 4. HERO SECTION ---
col_h1, col_h2 = st.columns([1.5, 1])
with col_h1:
    st.title("Data Analyst & AI Solutions Builder")
    st.write("I help businesses turn messy data into automated dashboards and AI agents.")
    st.markdown('<br><a href="#projects" class="hero-btn-primary">View My Projects</a> <a href="#contact" class="hero-btn-secondary">Work With Me</a>', unsafe_allow_html=True)
with col_h2:
    st.image("https://media.licdn.com/dms/image/v2/D5635AQE48RLqRqzU_Q/profile-framedphoto-shrink_400_400/B56ZpIecRlJsAc-/0/1762152531306?e=1767258000&v=beta&t=erhjntIohTme4sufbPVuugk8qRde4MEXW6OrO7S4PWE", width=300)

st.divider()

# --- 5. PROJECTS ---
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.header("Featured Projects")

with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    p1, p2 = st.columns([3, 1])
    with p1:
        st.subheader("✈️ Data Pilot: AI Data Analyst Agent")
        st.write("A private AI agent that cleans and visualizes CSV data using natural language.")
        st.write("**Tech:** Python, Streamlit, Gemini AI, Plotly")
    with p2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("🚀 Live Demo", "https://datapilot101.streamlit.app/", use_container_width=True)
        st.link_button("💻 Source Code", "https://github.com/raviodedara", use_container_width=True)
        st.link_button("🎥 How it Works", "https://x.com/your-video", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- 6. CONTACT FORM ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.header("Let's Work Together")

c1, c2 = st.columns(2)
with c1:
    st.write("📧 **Email:** ravikumargo2812@gmail.com")
    st.write("📍 **Location:** Canada")
    st.write("[LinkedIn](https://www.linkedin.com/in/ravikumar-odedara/) | [GitHub](https://github.com/raviodedara)")

with c2:
    # --- Formspree Integration ---
    # Replace 'YOUR_FORMSPREE_ID' with the ID from formspree.io
    form_id = "https://formspree.io/f/mdaonvwr" 
    
    st.markdown(f"""
        <form action="https://formspree.io/f/{form_id}" method="POST" style="background: white; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
            <label style="color:#333; font-weight:bold;">Name</label><br>
            <input type="text" name="name" required style="width:100%; padding:10px; margin-bottom:10px; border:1px solid #ccc; border-radius:5px;"><br>
            <label style="color:#333; font-weight:bold;">Email</label><br>
            <input type="email" name="_replyto" required style="width:100%; padding:10px; margin-bottom:10px; border:1px solid #ccc; border-radius:5px;"><br>
            <label style="color:#333; font-weight:bold;">Message</label><br>
            <textarea name="message" required style="width:100%; padding:10px; margin-bottom:10px; border:1px solid #ccc; border-radius:5px; height:100px;"></textarea><br>
            <button type="submit" style="background-color:#006666; color:white; border:none; padding:10px 20px; border-radius:5px; font-weight:bold; cursor:pointer; width:100%;">Send Message</button>
        </form>
    """, unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown("<br><hr><center><p style='color:#666;'>Ravi Odedara © 2025</p></center>", unsafe_allow_html=True)
