import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Normal Distribution Explorer", page_icon="📊", layout="wide")

# --- SESSION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- CSS ---

 
st.markdown("""
<style>
 [data-testid="stAppViewContainer"] {
    background-color: #4A90E2;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
body, .main {
    margin: 0;
    min-height: 100vh;
    width: 100vw;
    background-color: #4A90E2;
    overflow-x: hidden;
    overflow-y: auto;
}

/* Card */
.card {
    background-color: rgba(255,255,255,0.18);
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.5);
    padding: 60px 50px;
    width: 650px;
    text-align: center;
    box-shadow: 0 0 30px rgba(0,255,255,0.4);
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: white;
    margin-top: 20px;
    margin-bottom: 30px;
    opacity: 0;
}

/* Buttons */
div.stButton > button {
    background-color: white;
    color: #2b4c7e;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 18px;
    border: none;
}

/* Symbols */
.symbol {
    position: absolute;
    font-size: 20px;
    color: rgba(255,255,255,0.6);
    animation: drop linear infinite;
}

@keyframes drop {
    0% { transform: translateY(-50px); opacity:0; }
    10% { opacity:0.6; }
    100% { transform: translateY(110vh); opacity:0; }
}
</style>
""", unsafe_allow_html=True)

# --- SYMBOLS ---
def render_symbols():
    symbols = ["μ", "σ", "f(x)", "∫", "Σ", "π"]
    html = ""
    for _ in range(25):
        html += f"""
        <div class="symbol" 
        style="left:{random.randint(0,95)}%;
        animation-duration:{random.randint(8,20)}s;
        animation-delay:{random.uniform(0,10)}s;">
        {random.choice(symbols)}
        </div>
        """
    st.markdown(html, unsafe_allow_html=True)

render_symbols()

# --- NAVBAR ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home"):
        st.session_state.page = "home"
        st.rerun()

with col2:
    if st.button("Info"):
        st.session_state.page = "info"
        st.rerun()

with col3:
    if st.button("Graph"):
        st.session_state.page = "graph"
        st.rerun()

with col4:
    if st.button("Z-Score"):
        st.session_state.page = "zscore"
        st.rerun()

# --- CARD FUNCTION ---
def show_card(title_text, subtitle_text):
    placeholder = st.empty()
    text = ""

    for char in title_text:
        text += char
        placeholder.markdown(f"""
        <div style="height:100vh; display:flex; justify-content:center; align-items:center;">
            <div class="card">
                <h1 style="color:white; letter-spacing:5px;">{text}</h1>
                <p class="subtitle">{subtitle_text}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.03)

    st.markdown("""
    <style>
    .subtitle {opacity:1 !important;}
    </style>
    """, unsafe_allow_html=True)

    # ✅ EXPLORE BUTTON (ADDED)
    if st.button("📊 Explore"):
        st.session_state.page = "info"
        st.rerun()

# --- PAGES ---
if st.session_state.page == "home":
    show_card("NORMAL DISTRIBUTION", "Understand probability visually")

# --- INFO PAGE ---
elif st.session_state.page == "info":

    st.markdown("<h1 style='color:white; text-align:center;'>Normal Distribution</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.2); padding:20px; border-radius:15px;">
    <h3 style="color:white;">What is Normal Distribution?</h3>
    <p style="color:white;">
    Normal distribution is a probability distribution where data is symmetrically distributed around the mean.
    Most values are close to the average, forming a bell-shaped curve.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("<h3 style='color:white;'>Formula</h3>", unsafe_allow_html=True)
    st.latex(r"f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}")

    st.write("")
    st.markdown("<h3 style='color:white;'>Z-Score Formula</h3>", unsafe_allow_html=True)
    st.latex(r"z = \frac{x - \mu}{\sigma}")
    
    st.write("")
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.2); padding:20px; border-radius:15px;">
    <h3 style="color:white;">Key Idea</h3>
    <p style="color:white;">
    μ (mean) is the center and σ (standard deviation) controls spread.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown("<h2 style='color:white;'>Applications</h2>", unsafe_allow_html=True)

    if "selected_app" not in st.session_state:
        st.session_state.selected_app = None

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📊 Exams"):
            st.session_state.selected_app = "exams"
        if st.button("🧠 IQ"):
            st.session_state.selected_app = "iq"

    with col2:
        if st.button("📈 Finance"):
            st.session_state.selected_app = "finance"
        if st.button("🏥 Health"):
            st.session_state.selected_app = "health"

    st.write("")

    if st.session_state.selected_app == "exams":
        st.markdown("<p style='color:white;'>Most students score average marks forming a bell curve.</p>", unsafe_allow_html=True)
        st.image("exams.jpg", width=400)
    elif st.session_state.selected_app == "iq":
        st.markdown("<p style='color:white;'>IQ scores cluster around average.</p>", unsafe_allow_html=True)
        st.image("iq.jpg", width=400)

    elif st.session_state.selected_app == "finance":
        st.markdown("<p style='color:white;'>Used to analyze stock risks.</p>", unsafe_allow_html=True)
        st.image("finance.jpg", width=400)

    elif st.session_state.selected_app == "health":
        st.markdown("<p style='color:white;'>Used in medical measurements.</p>", unsafe_allow_html=True)
        st.image("health.png", width=400)

elif st.session_state.page == "graph":

    st.markdown("<h1 style='color:white; text-align:center;'>📊 Graph Analysis</h1>", unsafe_allow_html=True)

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm

    # --- SLIDERS ---
    col1, col2 = st.columns(2)

    with col1:
        mean = st.slider("Mean (μ)", -100.0, 100.0, 0.0)

    with col2:
        std = st.slider("Standard Deviation (σ)", 1.0, 50.0, 10.0)

    st.write("")

    # ✅ --- SELECT RULE (THIS IS NEW PART) ---
    rule = st.radio("Select Coverage", ["68%", "95%", "99.7%", "99.96%"])

    if rule == "68%":
     k = 1
    elif rule == "95%":
        k = 2
    elif rule == "99.7%":
        k = 3
    else:
        k = 3.5

    # --- REGION ---
    lower = mean - k * std
    upper = mean + k * std

    # --- DATA ---
    x = np.linspace(mean - 4*std, mean + 4*std, 1000)
    y = norm.pdf(x, mean, std)

    # --- PROBABILITY ---
    prob = norm.cdf(upper, mean, std) - norm.cdf(lower, mean, std)
    percent = prob * 100

    # --- GRAPH ---
    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(x, y, linewidth=3)

    # shaded region
    mask = (x >= lower) & (x <= upper)
    ax.fill_between(x[mask], y[mask], alpha=0.6)

    # mean line
    ax.axvline(mean, linestyle="--", linewidth=2)

    # std lines
    ax.axvline(lower, linestyle=":", linewidth=1)
    ax.axvline(upper, linestyle=":", linewidth=1)

    ax.set_title("Normal Distribution Curve")
    ax.set_xlabel("X")
    ax.set_ylabel("Density")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # --- RESULT ---
    st.markdown(f"""
    <h2 style='color:white; text-align:center;'>
    📊 {percent:.2f}% data lies within {k}σ from mean
    </h2>
    """, unsafe_allow_html=True)

    # --- INSIGHT ---
    if k == 1:
        msg = "Most common data (68% rule)"
    elif k == 2:
        msg = "Almost all data covered (95%)"
    elif k == 3:
        msg = "Extreme rare cases included (99.7%)"
    else:
        msg = "Nearly entire data covered (99.96%)"
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.2); padding:15px; border-radius:10px;">
    <p style="color:white; text-align:center;">{msg}</p>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "zscore":

    st.markdown("<h1 style='color:white; text-align:center;'>Z-Score & SNV Table</h1>", unsafe_allow_html=True)

    st.write("")

    # --- INPUT SECTION ---
    st.markdown("<h3 style='color:white;'>Enter Values</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        x = st.number_input("Value (x)", value=50.0)

    with col2:
        mean = st.number_input("Mean (μ)", value=50.0)

    with col3:
        std = st.number_input("Standard Deviation (σ)", min_value=0.1, value=10.0)

    st.write("")

    # --- Z CALCULATION ---
    z = (x - mean) / std

    st.markdown(f"""
    <div style="background-color: rgba(255,255,255,0.2); padding:20px; border-radius:15px;">
    <h3 style="color:white;">Z-Score Result</h3>
    <p style="color:white; font-size:22px;"><b>Z = {z:.3f}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # --- INTERPRETATION ---
    st.markdown("<h3 style='color:white;'>Interpretation</h3>", unsafe_allow_html=True)

    if z > 0:
        st.success("📈 Value is ABOVE the mean")
    elif z < 0:
        st.error("📉 Value is BELOW the mean")
    else:
        st.info("🎯 Value is EXACTLY at the mean")

    st.write("")

    # --- EXPLANATION BOX ---
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.2); padding:20px; border-radius:15px;">
    <p style="color:white;">
    Z-score tells how many standard deviations a value is from the mean.<br>
    Example:<br>
    Z = 2 → value is 2σ above mean<br>
    Z = -1 → value is 1σ below mean
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # --- OPTIONAL PROBABILITY ---
    try:
        from scipy.stats import norm
        prob = norm.cdf(z)

        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.2); padding:20px; border-radius:15px;">
        <h3 style="color:white;">Probability</h3>
        <p style="color:white;">P(X ≤ x) = {prob:.4f}</p>
        </div>
        """, unsafe_allow_html=True)
    except:
        st.warning("Install scipy to enable probability feature")

    st.write("")

    # --- SNV TABLE IMAGE ---
    st.markdown("<h2 style='color:white;'>Standard Normal Table (SNV)</h2>", unsafe_allow_html=True)

    st.image("snv.png", caption="Standard Normal Distribution Table", width=800)
    import numpy as np
    import matplotlib.pyplot as plt

    st.markdown("<h3 style='color:white;'>Z-Score Graph</h3>", unsafe_allow_html=True)

    # Generate values for curve
    x_vals = np.linspace(mean - 4*std, mean + 4*std, 1000)

    # Normal distribution formula
    y_vals = (1/(std * np.sqrt(2*np.pi))) * np.exp(-0.5*((x_vals - mean)/std)**2)

    # Create plot
    fig, ax = plt.subplots(figsize=(6, 4))  # smaller size

    # Plot curve
    ax.plot(x_vals, y_vals)

    # Mark user's value
    ax.axvline(x, linestyle='--')

    # Point on curve
    y_point = (1/(std * np.sqrt(2*np.pi))) * np.exp(-0.5*((x - mean)/std)**2)
    ax.scatter(x, y_point)

    # Show Z-score label
    ax.text(x, y_point, f" Z={z:.2f}")

    # Shade probability area
    ax.fill_between(x_vals, y_vals, where=(x_vals <= x), alpha=0.3)

    # Labels
    ax.set_title("Normal Distribution")
    ax.set_xlabel("Values")
    ax.set_ylabel("Density")

    st.pyplot(fig, use_container_width=False)
