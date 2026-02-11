import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Vibe", page_icon="🧬", layout="wide")

# --- HYPER-GENZ CYBER-STREETWEAR UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@300;700&family=DotGothic16&display=swap');

    .stApp {
        background: #000000;
        color: #ffffff;
    }

    /* Glitch Card Styling */
    .vibe-card {
        background: rgba(10, 10, 10, 0.95);
        border-left: 5px solid #00f2ff;
        border-right: 5px solid #7000ff;
        border-radius: 0px; /* Brutalist sharp edges */
        padding: 60px;
        box-shadow: 20px 20px 0px rgba(0, 242, 255, 0.1);
        max-width: 900px;
        margin: auto;
    }

    /* Gen-Z Hypebeast Title */
    .hype-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        text-align: left;
        line-height: 0.8;
        background: linear-gradient(90deg, #fff, #555, #00f2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -5px;
        margin-bottom: 20px;
        transform: skewX(-10deg);
    }

    .tag-line {
        font-family: 'DotGothic16', sans-serif;
        color: #7000ff;
        font-size: 1.2rem;
        margin-bottom: 40px;
        text-transform: uppercase;
    }

    /* Cyber Input */
    .stTextArea textarea {
        background: #0d0d0d !important;
        border: 2px solid #1a1a1a !important;
        border-radius: 0px !important;
        color: #fff !important;
        font-family: 'Space Grotesk', sans-serif !important;
        padding: 20px !important;
        font-size: 1.2rem !important;
    }

    /* High-Contrast Button */
    .stButton>button {
        background: #00f2ff;
        color: #000;
        border: none;
        padding: 30px;
        width: 100%;
        border-radius: 0px;
        font-family: 'Syncopate', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 5px;
        font-size: 1.2rem;
        transition: 0.2s;
        cursor: crosshair;
    }

    .stButton>button:hover {
        background: #7000ff;
        color: #fff;
        box-shadow: 10px 10px 0px #00f2ff;
        transform: translate(-5px, -5px);
    }

    .stCode {
        border-radius: 0px !important;
        background: #111 !important;
        border: 1px solid #333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE "VIBE-CHECK" BYPASS ENGINE ---
def vibe_humanize(text):
    # Phase 1: Slang & Filler Injection
    # AI hates these because they are 'inefficient'
    fillers = [" honestly, ", " basically, ", " like, ", " literally ", " lowkey "]
    
    def add_vibe(s):
        if len(s.split()) > 6 and random.random() > 0.4:
            words = s.split()
            words.insert(random.randint(1, 3), random.choice(fillers))
            return " ".join(words)
        return s

    # Phase 2: Structural Messiness
    # Replace robotic transitions with Gen-Z pivots
    text = re.sub(r'\bFurthermore\b', "Also, and another thing,", text, flags=re.IGNORECASE)
    text = re.sub(r'\bHowever\b', "But like,", text, flags=re.IGNORECASE)
    text = re.sub(r'\bTherefore\b', "So yeah,", text, flags=re.IGNORECASE)

    sentences = text.split(". ")
    final = []
    
    for i, s in enumerate(sentences):
        # Apply vibe-check
        s = add_vibe(s)
        
        # Every few sentences, add a "dramatic pause"
        if i % 3 == 0:
            s = s + "..."
            
        final.append(s)

    # Final bypass: Start with a personal 'Opinion' marker
    final.insert(0, "I personally feel like")
    
    return ". ".join(final).strip()

# --- INTERFACE ---
st.markdown('<div class="vibe-card">', unsafe_allow_html=True)
st.markdown('<h1 class="hype-title">SLANG<br>IFY.</h1>', unsafe_allow_html=True)
st.markdown('<p class="tag-line">// DETECTOR_KILLER_V7.0</p>', unsafe_allow_html=True)

user_data = st.text_area("", height=250, placeholder="PASTE_AI_DNA_HERE")

if st.button("BYPASS_SYSTEM"):
    if user_data:
        # Fun Gen-Z loading messages
        msg = st.empty()
        msgs = ["Sending vibe check...", "Killing the bot...", "Making it bussin...", "Ghosting the AI..."]
        for m in msgs:
            msg.markdown(f"<p style='color:#00f2ff;'>{m}</p>", unsafe_allow_html=True)
            time.sleep(0.5)
            
        processed = vibe_humanize(user_data)
        
        st.markdown("### // HUMAN_DNA_EXTRACTED")
        st.code(processed, language=None)
        st.success("100% VIBE. 0% ROBOT.")
    else:
        st.error("NO_INPUT_DETECTED")
st.markdown('</div>', unsafe_allow_html=True)
