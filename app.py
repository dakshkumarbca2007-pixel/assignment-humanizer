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
        background: radial-gradient(circle at top right, #000428, #004e92, #000000);
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
    }

    .main-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(25px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 35px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
        margin-top: 20px;
    }

    .liquid-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 3rem;
        text-align: center;
        background: linear-gradient(90deg, #00f2ff, #7000ff, #ff00c8, #00f2ff);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: liquidFlow 5s linear infinite;
        margin-bottom: 5px;
    }

    @keyframes liquidFlow {
        to { background-position: 300% center; }
    }

    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.4) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #00f2ff !important;
        padding: 15px !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #00f2ff, #7000ff);
        color: white;
        border: none;
        padding: 20px;
        width: 100%;
        border-radius: 50px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: 0.4s ease;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE 0% BYPASS ENGINE ---
def elite_humanizer(text):
    # Phase 1: Contextual Pattern Breaking
    replacements = {
        "furthermore": ["honestly,", "plus,", "also,"],
        "moreover": ["actually,", "and besides that,", "another thing is,"],
        "consequently": ["so basically,", "which means,"],
        "utilize": ["use", "go with"],
        "significant": ["major", "huge"],
        "essential": ["key", "needed"],
        "demonstrates": ["shows", "proves"]
    }
    
    for word, options in replacements.items():
        text = re.sub(rf'\b{word}\b', random.choice(options), text, flags=re.IGNORECASE)

    # Phase
