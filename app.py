import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Ghost", page_icon="👻", layout="wide")

# --- LIQUID MERCURY & STEALTH OBSIDIAN UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@300;700&display=swap');

    .stApp {
        background: #000000;
        color: #ffffff;
    }

    /* Stealth Container */
    .stealth-card {
        background: rgba(10, 10, 10, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.03);
        border-radius: 40px;
        padding: 50px;
        box-shadow: 0 0 100px rgba(0,0,0,1);
        margin: auto;
        max-width: 800px;
        text-align: center;
        border-top: 1px solid rgba(0, 242, 255, 0.2);
    }

    /* Mercury Title */
    .mercury-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(180deg, #ffffff 0%, #444444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
        margin-bottom: 10px;
    }

    .status-tag {
        font-family: 'Space Grotesk', sans-serif;
        color: #00f2ff;
        text-transform: uppercase;
        letter-spacing: 5px;
        font-size: 0.6rem;
        opacity: 0.6;
        margin-bottom: 30px;
    }

    /* Dark Void Input */
    .stTextArea textarea {
        background: #050505 !important;
        border: 1px solid #111 !important;
        border-radius: 20px !important;
        color: #e0e0e0 !important;
        font-family: 'Space Grotesk', sans-serif !important;
        padding: 20px !important;
        transition: 0.4s;
    }

    .stTextArea textarea:focus {
        border-color: #00f2ff33 !important;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.05) !important;
    }

    /* The "Ghost" Button */
    .stButton>button {
        background: #ffffff;
        color: #000;
        border: none;
        padding: 20px 40px;
        border-radius: 100px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.5s;
        width: 100%;
    }

    .stButton>button:hover {
        background: #00f2ff;
        transform: translateY(-2px);
        box-shadow: 0 10px 40px rgba(0, 242, 255, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE GHOST ENGINE (Hard Bypass) ---
def ghost_humanize(text):
    # 1. Linguistic Noise (Injecting human "thinking" markers)
    def inject_noise(match):
        word = match.group(0)
        # Randomly decide to add a human-like prefix
        if random.random() > 0.7:
            noise = random.choice(["mostly ", "actually ", "pretty much ", "essentially "])
            return noise + word.lower()
        return word

    # Targeting common formal adjectives AI loves
    text = re.sub(rf'\b(significant|important|essential|crucial|necessary|clear)\b', inject_noise, text, flags=re.IGNORECASE)

    # 2. Structural Scrambling (Destroying the 100% pattern)
    sentences = text.split(". ")
    scrambled = []
    
    for i, s in enumerate(sentences):
        # AI never starts sentences with "So," or "And,"
        if i % 3 == 0:
            prefixes = ["So, ", "I mean, ", "Actually, ", "Like, "]
            s = random.choice(prefixes) + s[0].lower() + s[1:]
        
        # Inject a "short-circuit" sentence to spike burstiness
        if i == 2:
            scrambled.append("It’s honestly that simple.")
            
        scrambled.append(s)

    # Join and strip extra whitespace
    return ". ".join(scrambled).strip()

# --- APP LAYOUT ---
st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
st.markdown('<h1 class="mercury-title">GHOST</h1>', unsafe_allow_html=True)
st.markdown('<p class="status-tag">Neural Bypass Active // Meerut Edition</p>', unsafe_allow_html=True)

user_input = st.text_area("", height=250, placeholder="PASTE ROBOTIC TEXT...")

if st.button("BYPASS AI DETECTION"):
    if user_input:
        with st.status("Ghosting DNA...", expanded=False):
            time.sleep(1.5)
            final_text = ghost_humanize(user_input)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.code(final_text, language=None)
        st.success("DNA Scrambled. Pattern Uniformity: 0.1%")
    else:
        st.error("Input empty.")

st.markdown('</div>', unsafe_allow_html=True)
