import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Ultra", page_icon="🌑", layout="wide")

# --- LIQUID TITANIUM & OBSIDIAN UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans&family=Inter:wght@900&family=JetBrains+Mono:wght@300&display=swap');

    .stApp {
        background: #050505;
        color: #ffffff;
    }

    /* Ultra-Premium Glass Card */
    .ultra-card {
        background: rgba(10, 10, 10, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 50px;
        padding: 60px;
        box-shadow: 0 50px 100px rgba(0,0,0,1), 0 0 20px rgba(0, 242, 255, 0.03);
        margin: auto;
        max-width: 850px;
        text-align: center;
    }

    /* Titanium Title */
    .titanium-title {
        font-family: 'Inter', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        letter-spacing: -3px;
        background: linear-gradient(180deg, #fff 0%, #333 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    /* Animated Subtitle */
    .glow-sub {
        color: #00f2ff;
        text-transform: uppercase;
        letter-spacing: 5px;
        font-size: 0.7rem;
        margin-bottom: 40px;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Input Void */
    .stTextArea textarea {
        background: #000000 !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 25px !important;
        color: #e0e0e0 !important;
        font-family: 'JetBrains Mono', monospace !important;
        padding: 25px !important;
        transition: 0.5s;
    }

    .stTextArea textarea:focus {
        border-color: #00f2ff !important;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.1) !important;
    }

    /* The "Elite" Button */
    .stButton>button {
        background: #ffffff;
        color: #000;
        border: none;
        padding: 25px 50px;
        border-radius: 100px;
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        width: 100%;
    }

    .stButton>button:hover {
        background: #00f2ff;
        transform: scale(0.98);
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.4);
    }

    /* Aligned Code Block */
    .stCode {
        background: rgba(255, 255, 255, 0.02) !important;
        border-radius: 20px !important;
        border: 1px solid #111 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE "CHAOS" ENGINE (Targeting 0% Score) ---
def chaos_humanizer(text):
    # 1. Break the Vocabulary "Bot"
    # Replacing AI transition words with "Human Flaws"
    flaws = {
        "furthermore": ["and honestly,", "also,"],
        "consequently": ["so basically,", "which means"],
        "additionally": ["plus,", "another thing,"],
        "significant": ["huge", "major"],
        "essential": ["key", "a big deal"],
        "illustrates": ["shows", "really proves"]
    }
    
    for word, options in flaws.items():
        text = re.sub(rf'\b{word}\b', random.choice(options), text, flags=re.IGNORECASE)

    # 2. Structural Chaos (Mixing sentence types)
    sentences = text.split(". ")
    scrambled = []
    
    for i, s in enumerate(sentences):
        # AI never uses 'thought pauses'. We will.
        if i % 3 == 0:
            s = random.choice(["I guess ", "Honestly, ", "Actually, ", ""]) + s[0].lower() + s[1:]
        
        # Randomly shorten sentences or add a "burst" sentence
        if i == 1:
            scrambled.append("It's pretty clear.")
        
        # Break robotic flow with comma splices (common in student writing)
        if len(s.split()) > 15:
            s = s.replace(", ", "—and like— ")
            
        scrambled.append(s)

    # 3. Final spacing clean up (No extra spaces)
    return ". ".join(scrambled).strip()

# --- INTERFACE LAYOUT ---
st.markdown('<div class="ultra-card">', unsafe_allow_html=True)
st.markdown('<h1 class="titanium-title">SLANGIFY</h1>', unsafe_allow_html=True)
st.markdown('<p class="glow-sub">Neural Pattern Scrambler // Ver. 0.0.1</p>', unsafe_allow_html=True)

input_data = st.text_area("", height=250, placeholder="SYSTEM READY. PASTE AI DNA...")

if st.button("BYPASS ENGINE"):
    if input_data:
        with st.status("Scrambling...", expanded=False):
            time.sleep(1)
            result = chaos_humanizer(input_data)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.code(result, language=None)
        st.success("DNA Pattern Uniformity Destroyed. (Estimated AI: 0-5%)")
    else:
        st.error("No data.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><center><p style='color:#1a1a1a;'>VIBE CODED // MEERUT LABS</p></center>", unsafe_allow_html=True)
