import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ravi Odedara | Data Analyst & AI Solutions",
    page_icon="RO",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CUSTOM CSS (The Design System) ---
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
    
    /* --- STICKY TOP NAVIGATION --- */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: white;
        padding: 15px 50px;
        z-index: 999;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar a {
        text-decoration: none;
        color: #333;
        font-weight: 600;
        margin-left: 25px;
        font-family: sans-serif;
        transition: color 0.3s;
    }
    .navbar a:hover {
        color: var(--accent-color);
    }
    .nav-logo {
        font-size: 1.5rem;
        font-weight: 900;
        color: var(--primary-color) !important;
    }
    
    /* Spacer to prevent content from hiding behind nav */
    .nav-spacer {
        height: 80px;
    }

    /* --- HERO SECTION --- */
    .hero-btn-primary {
        background-color: var(--accent-color);
        color: white !important;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .hero-btn-secondary {
        background-color: transparent;
        color: var(--primary-color) !important;
        border: 2px solid var(--primary-color);
        padding: 10px 22px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-left: 10px;
    }

    /* --- PROJECT CARDS --- */
    .project-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 5px solid var(--primary-color);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .project-card:hover {
        transform: translateY(-5px);
    }
    .tech-badge {
        background-color: #eef;
        color: #33a;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        margin-right: 5px;
        font-weight: 600;
    }

    /* --- SERVICES --- */
    .service-box {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #eee;
        height: 100%;
    }

    /* --- CONTACT FORM --- */
    input, textarea {
        border-radius: 5px;
        border: 1px solid #ddd;
        padding: 10px;
        width: 100%;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. NAVIGATION BAR (HTML) ---
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

col_hero_text, col_hero_img = st.columns([1.5, 1])

with col_hero_text:
    st.markdown("# Data Analyst & AI Solutions Builder")
    st.markdown("### Helping Businesses Automate Data Workflows")
    st.write("""
    I help small and mid-sized businesses turn messy data into automated, insight-rich dashboards 
    and AI agents that save 10–20 hours per week. Combining an MBA in Business Analytics 
    with hands-on AI engineering to deliver operational efficiency.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Hero Buttons
    st.markdown("""
        <a href="#projects" class="hero-btn-primary">View My Projects</a>
        <a href="#contact" class="hero-btn-secondary">Work With Me</a>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    # Social Proof / Trust
    st.caption("TRUSTED BY TEAMS AT: Shoppers Drug Mart • Shanti Business School")

with col_hero_img:
    # PLACEHOLDER: Replace this URL with your actual photo
    st.image("file:///C:/Users/Owner/Desktop/Wallpaper/WhatsApp%20Image%202025-09-23%20at%2019.18.11_fc0fa7b9.jpg", width=400)

st.divider()

# --- 5. ABOUT SECTION ---
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.header("About Me")

col_about, col_highlights = st.columns([2, 1])

with col_about:
    st.write("""
    I am a Data Analyst & AI-focused Business Analyst based in **Burnaby, BC**.
    
    **My Specialty:** I specialize in automating reporting, building dashboards, and creating AI-powered agents 
    for retail, education, and small business operations.
    
    **The Unique Combo:**
    * 📘 **Strong Math Background** (B.Sc. Math)
    * 📊 **MBA in Business Analytics**
    * 🤖 **Real-world Ops + AI Tooling Experience**
    """)
    
    # Personal Touch
    st.info("💡 **Fun Fact:** When I'm not building AI agents, I enjoy hiking the trails around Burnaby Mountain.")

with col_highlights:
    st.markdown("### ⚡ What I'm Good At")
    st.markdown("""
    * ✅ Automating recurring reports & KPIs
    * ✅ Building interactive dashboards
    * ✅ Designing AI copilots for data teams
    * ✅ Cleaning messy operational data
    """)
    # Resume Button
    st.link_button("📄 Download Resume", "https://linkedin.com/in/your-profile", help="Link to PDF Resume")

st.divider()

# --- 6. SKILLS SECTION ---
st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
st.header("Technical Skills")
st.write("I use these tools to move from **raw data → clean dataset → analysis → automated dashboards**.")

skill_c1, skill_c2 = st.columns(2)

with skill_c1:
    st.subheader("🛠️ Tools & Languages")
    st.write("**Python:** Pandas, NumPy, Matplotlib, Seaborn")
    st.write("**SQL:** Complex Queries, Joins, Aggregation")
    st.write("**Excel:** Advanced Formulas, Pivot Tables, VBA")
    st.write("**BI:** Power BI, Tableau, Streamlit")

with skill_c2:
    st.subheader("🤖 AI & Automation")
    st.write("**Gen AI:** Prompt Engineering, Gemini 1.5 Pro")
    st.write("**Agents:** Custom AI Agent Design, RAG")
    st.write("**Cloud:** AWS (Basic EC2/S3 deployment)")
    st.write("**Process:** Data Cleaning, KPI Definition, Time-Series")

st.divider()

# --- 7. PROJECTS SECTION ---
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.header("Featured Projects")

# --- PROJECT 1: DATA PILOT ---
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    p1_c1, p1_c2 = st.columns([3, 1])
    with p1_c1:
        st.subheader("✈️ Data Pilot: AI Data Analyst Agent")
        st.write("**Summary:** A private AI agent that allows users to clean, map, and visualize CSV data using natural language.")
        st.write("**Problem:** Small teams spend 80% of time cleaning data and fear uploading sensitive files to public AI.")
        st.write("**My Approach:** Built a 'Bring Your Own Key' Streamlit app with 'Safe-Mode' architecture to prevent data loss.")
        st.write("**Outcome:** Reduces data cleaning time by ~90% for non-technical users.")
        st.markdown("**Tech:** <span class='tech-badge'>Python</span> <span class='tech-badge'>Streamlit</span> <span class='tech-badge'>Gemini AI</span> <span class='tech-badge'>Plotly</span>", unsafe_allow_html=True)
    with p1_c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("🚀 Live Demo", "https://datapilot101.streamlit.app/", use_container_width=True)
        st.link_button("💻 Source Code", "https://github.com/your-repo", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PROJECT 2: RETAIL DASHBOARD (Placeholder) ---
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    p2_c1, p2_c2 = st.columns([3, 1])
    with p2_c1:
        st.subheader("🛒 Retail Inventory Optimization Dashboard")
        st.write("**Summary:** Automated inventory tracking system for a multi-store retail chain.")
        st.write("**Problem:** Store managers were manually updating weekly sales reports, taking ~6 hours/week.")
        st.write("**My Approach:** Built automated Python pipeline to pull data and generate Tableau dashboards.")
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
    st.markdown('<div class="service-box">', unsafe_allow_html=True)
    st.subheader("📊 Reporting Automation")
    st.write("Stop copy-pasting Excel rows. I automate your weekly/monthly KPI reports so they arrive in your inbox automatically.")
    st.markdown("*Time saved: 5-10 hours/week*")
    st.markdown('</div>', unsafe_allow_html=True)

with serv_c2:
    st.markdown('<div class="service-box">', unsafe_allow_html=True)
    st.subheader("📈 Interactive Dashboards")
    st.write("I build central dashboards (Power BI/Streamlit) so you can see Sales, Inventory, and Ops data in one place.")
    st.markdown("*Better visibility on KPIs*")
    st.markdown('</div>', unsafe_allow_html=True)

with serv_c3:
    st.markdown('<div class="service-box">', unsafe_allow_html=True)
    st.subheader("🤖 Custom AI Agents")
    st.write("I build private AI tools that 'chat' with your data, allowing your team to ask questions without knowing SQL.")
    st.markdown("*Typical project: 2-4 weeks*")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><center>", unsafe_allow_html=True)
st.markdown('<a href="#contact" class="hero-btn-primary">Request a Quote</a>', unsafe_allow_html=True)
st.markdown("</center><br>", unsafe_allow_html=True)

st.divider()

# --- 9. CONTACT SECTION ---
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.header("Let's Work Together")

contact_c1, contact_c2 = st.columns([1, 1])

with contact_c1:
    st.write("Interested in working together or hiring me full-time? Let's talk.")
    st.write("📧 **Email:** ravi.odedara@example.com") # REPLACE WITH YOUR EMAIL
    st.write("📍 **Location:** Burnaby, BC, Canada")
    st.write("⏱️ **Response Time:** Usually within 24 hours.")
    
    st.markdown("### Connect")
    st.write("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

with contact_c2:
    st.markdown("### Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            st.success("Thanks! I'll get back to you shortly.")

# --- 10. FOOTER ---
st.markdown("""
    <hr>
    <div style="text-align:center; color: #666; padding: 20px;">
        <p>Ravi Odedara © 2025 • Burnaby, BC, Canada</p>
        <p>
            <a href="#home" style="color:#666; text-decoration:none;">Home</a> | 
            <a href="#projects" style="color:#666; text-decoration:none;">Projects</a> | 
            <a href="#contact" style="color:#666; text-decoration:none;">Contact</a>
        </p>
    </div>
""", unsafe_allow_html=True)
