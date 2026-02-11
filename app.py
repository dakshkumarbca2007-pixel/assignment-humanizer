import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Phantom", page_icon="👻", layout="wide")

# --- FUTURISTIC LIQUID GLASS & CHROME CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Space+Grotesk:wght@300;500&display=swap');

    /* Background: Deep Obsidian Gradient */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #050505 0%, #000000 100%);
        color: #e0e0e0;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Insane Liquid Glass Container */
    .phantom-card {
        background: rgba(255, 255, 255, 0.01);
        backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 40px;
        padding: 60px;
        box-shadow: 0 40px 100px rgba(0, 0, 0, 0.9);
        margin: auto;
        max-width: 900px;
        animation: neon-breathe 8s ease-in-out infinite;
    }

    @keyframes neon-breathe {
        0%, 100% { border-color: rgba(0, 242, 255, 0.1); box-shadow: 0 0 20px rgba(0, 242, 255, 0.05); }
        50% { border-color: rgba(112, 0, 255, 0.3); box-shadow: 0 0 50px rgba(112, 0, 255, 0.1); }
    }

    /* Title: Chrome Flow */
    .phantom-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #fff 30%, #555 50%, #fff 70%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 4s linear infinite;
        letter-spacing: 10px;
    }

    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* Input: Dark Void */
    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.8) !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 20px !important;
        color: #00f2ff !important;
        font-size: 1.1rem !important;
        padding: 20px !important;
        line-height: 1.6 !important;
    }

    /* Button: Liquid Metal */
    .stButton>button {
        background: #ffffff;
        color: #000;
        border: none;
        padding: 25px 0;
        width: 100%;
        border-radius: 100px;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 5px;
        transition: 0.6s cubic-bezier(0.19, 1, 0.22, 1);
        cursor: pointer;
    }

    .stButton>button:hover {
        background: #00f2ff;
        color: #000;
        box-shadow: 0 0 80px rgba(0, 242, 255, 0.5);
        transform: scale(1.02);
    }

    /* Result Box Aligned Perfectly */
    .stCode {
        background: rgba(0, 0, 0, 0.9) !important;
        border-radius: 25px !important;
        border: 1px solid #333 !important;
        padding: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE 0% PHANTOM ENGINE ---
def phantom_humanize(text):
    # 1. Linguistic Scrambling (Contextual Synonyms)
    replacements = {
        "furthermore": "also, like,", "moreover": "and honestly,",
        "utilize": "go with", "essential": "key",
        "demonstrates": "pretty much shows", "consequently": "so yeah,",
        "significant": "huge", "very": "really", "however": "but then again,"
    }
    
    # 2. Add 'Human Stutter' & 'Filler' Particles
    fillers = ["I feel like ", "Basically, ", "Actually, ", "The thing is, "]
    short_bursts = ["It makes sense.", "Right?", "That's the point.", "Just saying."]

    for old, new in replacements.items():
        text = re.sub(rf'\b{old}\b', new, text, flags=re.IGNORECASE)

    sentences = text.split(". ")
    final_sentences = []

    for i, s in enumerate(sentences):
        # Inject Burstiness (Short/Long variation)
        if i % 4 == 0:
            final_sentences.append(random.choice(short_bursts))
        
        # Inject conversational randomness
        if len(s.split()) > 10:
            s = random.choice(fillers) + s[0].lower() + s[1:]
        
        # Random lower-casing of non-critical nouns to look like human typing
        s = s.replace("This ", "this ").replace("The ", "the ") if random.random() > 0.7 else s
        
        final_sentences.append(s)

    # Rejoin with standard spacing (AI detectors flag extra spaces too)
    return ". ".join(final_sentences).strip()

# --- INTERFACE ---
st.markdown('<h1 class="phantom-title">SLANGIFY PHANTOM</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#555; letter-spacing:5px;">ZERO-POINT STEALTH ENGINE v6.0</p>', unsafe_allow_html=True)

st.markdown('<div class="phantom-card">', unsafe_allow_html=True)

input_box = st.text_area("", height=250, placeholder="SYSTEM READY. PASTE AI DNA...")

if st.button("EXECUTE BYPASS ⚡"):
    if input_box:
        progress_bar = st.progress(0)
        for p in range(101):
            time.sleep(0.01)
            progress_bar.progress(p)
            
        output = phantom_humanize(input_box)
        
        st.markdown("### 🧬 DECODED HUMAN DNA")
        # st.code provides a native, perfectly aligned "Copy" button
        st.code(output, language=None)
        
        st.success("ENCRYPTION BROKEN. AI SCORE: 0% ESTIMATED.")
    else:
        st.error("NO DNA DETECTED.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><center><p style='color:#222;'>LAB PROTOCOL 006 • FUTURISTIC ED.</p></center>", unsafe_allow_html=True)
