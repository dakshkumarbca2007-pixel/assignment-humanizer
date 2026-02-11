import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify X", page_icon="⚡", layout="centered")

# --- NEO-LIQUID GLASS UI (2026 STYLE) ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #000428, #004e92);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    /* Liquid Glass Container */
    .liquid-glass {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px) saturate(180%);
        border-radius: 30px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 10px 50px rgba(0, 0, 0, 0.5);
        margin: 20px 0;
    }
    /* Neon Glow Input */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid #00f2ff55 !important;
        border-radius: 15px !important;
        color: #00f2ff !important;
        box-shadow: inset 0 0 10px #00f2ff11;
    }
    /* Magnetic Liquid Button */
    .stButton>button {
        background: linear-gradient(135deg, #00f2ff, #7000ff);
        color: white;
        border: none;
        padding: 18px;
        border-radius: 60px;
        font-weight: 900;
        letter-spacing: 2px;
        transition: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 0 30px rgba(112, 0, 255, 0.6);
    }
    .stButton>button:hover {
        transform: scale(1.05) rotate(-1deg);
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# --- STEALTH BYPASS ENGINE ---
def stealth_humanize(text):
    # Phase 1: Complexity Mapping
    # Replacing formal markers with "messy" human alternatives
    patterns = {
        "furthermore": ["and honestly,", "also,", "on top of that,"],
        "moreover": ["plus,", "actually,", "wait, also,"],
        "utilize": ["use", "go with", "mess around with"],
        "consequently": ["so,", "which basically means", "as a result,"],
        "significant": ["huge", "major", "crazy important"],
        "essential": ["key", "a big deal", "needed"],
    }
    
    for word, options in patterns.items():
        text = re.sub(rf'\b{word}\b', random.choice(options), text, flags=re.IGNORECASE)

    # Phase 2: Burstiness Injection (Rhythm Breaking)
    sentences = text.split(". ")
    human_blocks = []
    
    for i, s in enumerate(sentences):
        # AI always writes 15-20 words. Humans write 3 words, then 30 words.
        if i % 3 == 0: 
            human_blocks.append(random.choice(["It's true.", "I guess.", "Basically.", "Look."]))
        
        # Randomly lower the case of the first word to mimic 'fast typing'
        if random.random() > 0.8:
            s = s[0].lower() + s[1:]
            
        human_blocks.append(s)
            
    return ". ".join(human_blocks)

# --- APP LAYOUT ---
st.markdown('<div class="liquid-glass">', unsafe_allow_html=True)
st.title("⚡ SLANGIFY X")
st.write("### AI Bypass Engine | Liquid Glass v4.2")

input_data = st.text_area("Paste Content to Scramble:", height=200)

if st.button("EXECUTE STEALTH BYPASS 🛡️"):
    if input_data.strip():
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
            
        final_output = stealth_humanize(input_data)
        
        st.markdown("### 🧬 Scrambled DNA:")
        st.code(final_output, language=None)
        
        st.success("Bypass Active. Pattern Uniformity Destroyed.")
    else:
        st.error("Input missing, captain.")
st.markdown('</div>', unsafe_allow_html=True)
