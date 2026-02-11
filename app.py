import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Stealth X", page_icon="🕶️", layout="centered")

# --- INSANE LIQUID CHROME & GLASS UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@300;500;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #000428 0%, #004e92 100%);
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Glassmorphic Main Card */
    .main-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(30px) saturate(200%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 40px;
        padding: 50px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6);
        animation: slideUp 1s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0px); }
    }

    /* Neon Liquid Title */
    .liquid-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 2.8rem;
        text-align: center;
        background: linear-gradient(90deg, #00f2ff, #7000ff, #ff00c8, #00f2ff);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: liquidFlow 4s linear infinite;
        margin-bottom: 5px;
    }

    @keyframes liquidFlow {
        to { background-position: 300% center; }
    }

    /* Premium Input Area */
    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.5) !important;
        border: 2px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 20px !important;
        color: #00f2ff !important;
        padding: 20px !important;
        font-size: 1.1rem !important;
        transition: 0.3s;
    }

    .stTextArea textarea:focus {
        border-color: #7000ff !important;
        box-shadow: 0 0 20px rgba(112, 0, 255, 0.4) !important;
    }

    /* Chrome Magnetic Button */
    .stButton>button {
        background: linear-gradient(90deg, #00f2ff, #7000ff);
        color: white;
        border: none;
        padding: 22px;
        width: 100%;
        border-radius: 100px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 4px;
        transition: 0.5s;
        box-shadow: 0 10px 30px rgba(0, 242, 255, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(112, 0, 255, 0.7);
        letter-spacing: 6px;
    }

    /* Perfectly Aligned Output Box */
    .stCode {
        border-radius: 20px !important;
        border: 1px solid rgba(112, 0, 255, 0.5) !important;
        background: rgba(0, 0, 0, 0.8) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 0% DETECTION BYPASS ENGINE ---
def ultimate_humanize(text):
    # 1. Linguistic 'De-Optimization' (Breaking AI predictability)
    replacements = {
        "furthermore": "also,", "moreover": "plus,", 
        "consequently": "so basically,", "utilize": "use",
        "significant": "huge", "essential": "key",
        "demonstrates": "shows", "in conclusion": "long story short,"
    }
    
    # Randomly swap formal words for 'chatty' human words
    for ai_word, human_word in replacements.items():
        text = re.sub(rf'\b{ai_word}\b', human_word, text, flags=re.IGNORECASE)

    # 2. 'Burstiness' Injection (The 0% Secret)
    # AI uses equal sentence lengths. We will mix tiny sentences with long ones.
    sentences = text.split(". ")
    humanized = []
    
    for i, s in enumerate(sentences):
        # Every 3rd sentence, we inject a very human "thought particle"
        if i % 3 == 0:
            fillers = ["I mean, ", "Actually, ", "Like, ", "Basically, "]
            s = random.choice(fillers) + s[0].lower() + s[1:]
        
        # Randomly remove capital letters at start (texting style)
        if random.random() > 0.85:
            s = s[0].lower() +
