import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ravi Odedara | Data Analyst & AI Solutions",
    page_icon="RO",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. THE ULTIMATE DESIGN SYSTEM (CSS) ---
st.markdown("""
    <style>
    /* --- COLORS & FONTS --- */
    :root {
        --primary-color: #006666; /* Deep Teal */
        --accent-color: #FF4B4B; /* Coral/Orange */
        --bg-color: #F8F9FA; /* Light Gray/White */
        --text-color: #333333;
    }
    
    /* Global Styles */
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-color);
    }
    h1, h2, h3 {
        color: var(--primary-color) !important;
    }
    p, li {
        color: #444444 !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }

    /* --- NUCLEAR BUTTON FIX (Forces Teal & White Text) --- */
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
        font-weight: bold !important;
    }

    /* Hover effects for all */
    [data-testid="stLinkButton"]:hover, button:hover {
        background-color: #004d4d !important;
        transform: translateY(-2px) !important;
    }
    
    /* --- STICKY TOP NAVIGATION --- */
    .navbar {
        position: fixed; top: 0; left: 0; width: 100%; background-color: white;
        padding: 15px 50px; z-index: 999; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        display: flex; justify-content: space-between; align-items: center;
    }
    .navbar a {
        text-decoration: none; color: #333; font-weight: 600; margin-left: 25px;
        font-family: sans-serif; transition: color 0.3s;
    }
    .navbar a:hover { color: var(--accent-color); }
    .nav-logo { font-size: 1.5rem; font-weight: 900; color: var(--primary-color) !important; }
    .nav-spacer { height: 80px; }

    /* --- HERO SECTION --- */
    .hero-btn-primary {
        background-color: var(--accent-color); color: white !important;
        padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold;
        display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .hero-btn-secondary {
        background-color: transparent; color: var(--primary-color) !important;
        border: 2px solid var(--primary-color); padding: 10px 22px; border-radius: 8px;
        text-decoration: none; font-weight: bold; display: inline-block; margin-left: 10px;
    }

    /* --- PROJECT CARDS --- */
    .project-card {
        background-color: white; padding: 25px; border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid var(--primary-color);
        margin-bottom: 20px;
    }
    .tech-badge {
        background-color: #eef; color: #33a; padding: 4px 8px; border-radius: 4px;
        font-size: 0.8rem; margin-right: 5px; font-weight: 600;
    }

    /* --- SERVICES BOX --- */
    .service-box {
        background-color: white; padding: 30px; border-radius: 10px;
        text-align: center; border: 1px solid #eee; height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. NAVIGATION BAR ---
st.markdown("""
    <div class="navbar">
        <div class="nav-logo">RO</div>
        <div>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    <div class="nav-spacer"></div>
""", unsafe_allow_html=True)

# --- 4. HERO SECTION ---
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
col_h_text, col_h_img = st.columns([1.5, 1])

with col_h_text:
    st.markdown("# Data Analyst & AI Solutions Builder")
    st.markdown("### Helping Businesses Automate Data Workflows")
    st.write("""
    I help small and mid-sized businesses turn messy data into automated, insight-rich dashboards 
    and AI agents that save 10–20 hours per week. Combining an MBA in Business Analytics 
    with hands-on AI engineering to deliver operational efficiency.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <a href="#projects" class="hero-btn-primary">View My Projects</a>
        <a href="#contact" class="hero-btn-secondary">Work With Me</a>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("TRUSTED BY TEAMS AT: JadeBlue E-Comm. • Shanti B School")

with col_h_img:
    st.image("https://media.licdn.com/dms/image/v2/D5635AQE48RLqRqzU_Q/profile-framedphoto-shrink_400_400/B56ZpIecRlJsAc-/0/1762152531306?e=1767258000&v=beta&t=erhjntIohTme4sufbPVuugk8qRde4MEXW6OrO7S4PWE", width=350)

st.divider()

# --- 5. ABOUT SECTION ---
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.header("About Me")
col_a, col_h = st.columns([2, 1])

with col_a:
    st.write("""
    I am a Data Analyst & AI-focused Business Analyst based in **Canada**.
    
    **My Specialty:** I specialize in automating reporting, building dashboards, and creating AI-powered agents 
    for retail, education, and small business operations.
    
    **The Unique Combo:**
    * 📘 **Strong Math Background** (B.Sc. Math)
    * 📊 **MBA in Business Analytics**
    * 🤖 **Real-world Ops + AI Tooling Experience**
    """)
    st.info("💡 **Fun Fact:** When I'm not building AI agents, I enjoy hiking the trails around Burnaby Mountain.")

with col_h:
    st.markdown("### ⚡ What I'm Good At")
    st.markdown("""
    * ✅ Automating recurring reports & KPIs
    * ✅ Building interactive dashboards
    * ✅ Designing AI copilots for data teams
    * ✅ Cleaning messy operational data
    """)
    st.link_button("📄 Download Resume", "https://www.linkedin.com/in/ravikumar-odedara/")

st.divider()

# --- 6. SKILLS SECTION ---
st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
st.header("Technical Skills")
s_c1, s_c2 = st.columns(2)

with s_c1:
    st.subheader("🛠️ Tools & Languages")
    st.write("**Python:** Pandas, NumPy, Matplotlib, Seaborn")
    st.write("**SQL:** Complex Queries, Joins, Aggregation")
    st.write("**Excel:** Advanced Formulas, Pivot Tables, VBA")
    st.write("**BI:** Power BI, Tableau, Streamlit")

with s_c2:
    st.subheader("🤖 AI & Automation")
    st.write("**Gen AI:** Prompt Engineering, Gemini 1.5 Pro")
    st.write("**Agents:** Custom AI Agent Design, RAG")
    st.write("**Cloud:** AWS (Basic EC2/S3 deployment)")
    st.write("**Process:** Data Cleaning, KPI Definition, Time-Series")

st.divider()

# --- 7. PROJECTS SECTION ---
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.header("Featured Projects")

# Data Pilot Project
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    p1_c1, p1_c2 = st.columns([3, 1])
    with p1_c1:
        st.subheader("✈️ Data Pilot: AI Data Analyst Agent")
        st.write("**Summary:** A private AI agent that allows users to clean, map, and visualize CSV data using natural language.")
        st.write("**Problem:** Small teams spend 80% of time cleaning data and fear sensitive files in public AI.")
        st.write("**My Approach:** Built a 'Bring Your Own Key' Streamlit app with 'Safe-Mode' architecture to prevent data loss.")
        st.write("**Outcome:** Reduces data cleaning time by ~90% for non-technical users.")
        st.markdown("**Tech:** <span class='tech-badge'>Python</span> <span class='tech-badge'>Streamlit</span> <span class='tech-badge'>Gemini AI</span>", unsafe_allow_html=True)
    with p1_c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("🚀 Live Demo", "https://datapilot101.streamlit.app/", use_container_width=True)
        st.link_button("💻 Source Code", "https://github.com/raviodedara", use_container_width=True)
        st.link_button("🎥 How it Works", "https://x.com/your-video", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Retail Dashboard Project
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    p2_c1, p2_c2 = st.columns([3, 1])
    with p2_c1:
        st.subheader("🛒 Retail Inventory Optimization Dashboard")
        st.write("**Summary:** Automated inventory tracking system for a multi-store retail chain.")
        st.write("**Problem:** Managers manually updating sales reports, taking ~6 hours/week.")
        st.write("**Outcome:** Reduced reporting time by 70%, freeing up 4 hours/week per manager.")
        st.markdown("**Tech:** <span class='tech-badge'>Python</span> <span class='tech-badge'>Tableau</span> <span class='tech-badge'>Excel</span>", unsafe_allow_html=True)
    with p2_c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("View Details", key="p2_btn", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- 8. SERVICES SECTION ---
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.header("How I Can Help Your Business")
serv_c1, serv_c2, serv_c3 = st.columns(3)

with serv_c1:
    st.markdown('<div class="service-box"><h3>📊 Reporting Automation</h3><p>Stop copy-pasting Excel rows. I automate your monthly KPI reports so they arrive in your inbox automatically.</p><p><i>Time saved: 5-10 hours/week</i></p></div>', unsafe_allow_html=True)
with serv_c2:
    st.markdown('<div class="service-box"><h3>📈 Interactive Dashboards</h3><p>I build central dashboards (Power BI/Streamlit) so you can see Sales, Inventory, and Ops data in one place.</p></div>', unsafe_allow_html=True)
with serv_c3:
    st.markdown('<div class="service-box"><h3>🤖 Custom AI Agents</h3><p>I build private AI tools that chat with your data, allowing your team to ask questions without knowing SQL.</p></div>', unsafe_allow_html=True)

st.markdown("<br><center><a href='#contact' class='hero-btn-primary'>Request a Quote</a></center><br>", unsafe_allow_html=True)

st.divider()

# --- 9. CONTACT SECTION (FUNCTIONAL FORMSPREE) ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.header("Let's Work Together")
c_c1, c_c2 = st.columns(2)

with c_c1:
    st.write("Interested in working together or hiring me full-time? Let's talk.")
    st.write("📧 **Email:** ravikumargo2812@gmail.com")
    st.write("📍 **Location:** Canada")
    st.write("[LinkedIn](https://www.linkedin.com/in/ravikumar-odedara/) | [GitHub](https://github.com/raviodedara)")

with c_c2:
    # REPLACE 'YOUR_ID' with your ID from formspree.io
    form_id = "https://formspree.io/f/mdaonvwr" 
    st.markdown(f"""
        <form action="https://formspree.io/f/{form_id}" method="POST" style="background:white; padding:20px; border-radius:10px; border:1px solid #ddd;">
            <label style="color:#333; font-weight:bold;">Name</label><br>
            <input type="text" name="name" required style="width:100%; padding:8px; margin-bottom:10px; border:1px solid #ccc; border-radius:5px;"><br>
            <label style="color:#333; font-weight:bold;">Email</label><br>
            <input type="email" name="_replyto" required style="width:100%; padding:8px; margin-bottom:10px; border:1px solid #ccc; border-radius:5px;"><br>
            <label style="color:#333; font-weight:bold;">Message</label><br>
            <textarea name="message" required style="width:100%; padding:8px; margin-bottom:10px; border:1px solid #ccc; border-radius:5px; height:80px;"></textarea><br>
            <button type="submit" style="background-color:#006666; color:white; border:none; padding:10px; border-radius:5px; font-weight:bold; cursor:pointer; width:100%;">Send Message</button>
        </form>
    """, unsafe_allow_html=True)

# --- 10. FOOTER ---
st.markdown("<hr><center><p style='color:#666;'>Ravi Odedara © 2025 • Canada</p></center>", unsafe_allow_html=True)
