import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Phantom Ultra", page_icon="🌑", layout="wide")

# --- INSANE CARBON & LIQUID CHROME UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=JetBrains+Mono:wght@300;700&display=swap');

    .stApp {
        background: #000000;
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Animated Carbon Card */
    .phantom-card {
        background: linear-gradient(145deg, #0a0a0a 0%, #050505 100%);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 40px;
        padding: 60px;
        box-shadow: 0 40px 100px rgba(0,0,0,1);
        max-width: 850px;
        margin: auto;
        position: relative;
        overflow: hidden;
    }

    /* Moving Border Glow */
    .phantom-card::after {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 40px;
        border: 2px solid transparent;
        background: linear-gradient(90deg, transparent, rgba(0, 242, 255, 0.2), transparent) border-box;
        -webkit-mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: destination-out;
        mask-composite: exclude;
        animation: border-flow 4s linear infinite;
    }

    @keyframes border-flow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }

    /* Liquid Chrome Title */
    .chrome-header {
        font-family: 'Syncopate', sans-serif;
        font-size: 4.2rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(180deg, #fff 20%, #444 60%, #fff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -5px;
        margin-bottom: 0px;
        filter: drop-shadow(0 0 10px rgba(255,255,255,0.2));
    }

    /* Input Styling */
    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.8) !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 20px !important;
        color: #00f2ff !important;
        padding: 25px !important;
        font-size: 1rem !important;
        transition: 0.5s;
    }

    /* The "Ghost" Button */
    .stButton>button {
        background: #ffffff;
        color: #000;
        border: none;
        padding: 25px;
        width: 100%;
        border-radius: 100px;
        font-family: 'Syncopate', sans-serif;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 4px;
        transition: 0.4s cubic-bezier(0.19, 1, 0.22, 1);
        margin-top: 20px;
    }

    .stButton>button:hover {
        background: #00f2ff;
        transform: scale(0.97) translateY(2px);
        box-shadow: 0 0 60px rgba(0, 242, 255, 0.5);
    }

    /* Copy-Ready Code Area */
    .stCode {
        border-radius: 20px !important;
        background: #000000 !important;
        border: 1px solid #111 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 0% BYPASS ENGINE: "STRUCTURAL JITTER" ---
def ultra_humanize(text):
    # Phase 1: Contextual Scrambling
    def jitter_logic(s):
        # AI never uses these 'pivot' words correctly
        pivots = ["honestly ", "kind of ", "pretty much ", "literally "]
        words = s.split()
        if len(words) > 7 and random.random() > 0.5:
            words.insert(random.randint(2, 5), random.choice(pivots))
        return " ".join(words)

    # Clean formal transitions that flag AI
    text = re.sub(r'\bFurthermore\b', "Also,", text, flags=re.IGNORECASE)
    text = re.sub(r'\bConsequently\b', "So basically,", text, flags=re.IGNORECASE)
    text = re.sub(r'\bUtilize\b', "use", text, flags=re.IGNORECASE)

    # Phase 2: Structural Chaos
    sentences = text.split(". ")
    final = []
    
    for i, s in enumerate(sentences):
        # Breaking the rhythm
        s = jitter_logic(s)
        
        # Injecting a "Short Burst" to kill AI predictability
        if i == 1:
            final.append("It's just how things are.")
            
        final.append(s)

    # Phase 3: "I" Statement Injection (Detector Killer)
    final.insert(0, "From what I've seen,")
    
    return ". ".join(final).strip()

# --- APP LAYOUT ---
st.markdown('<div class="phantom-card">', unsafe_allow_html=True)
st.markdown('<h1 class="chrome-header">PHANTOM</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00f2ff; letter-spacing:10px; font-size:0.6rem; margin-bottom:40px; opacity:0.6;">CARBON PROTOCOL // 0% DETECT</p>', unsafe_allow_html=True)

user_input = st.text_area("", height=240, placeholder="SYSTEM READY. PASTE DNA...")

if st.button("EXECUTE BYPASS"):
    if user_input:
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
            
        processed = ultra_humanize(user_input)
        
        st.markdown("### 🧬 HUMANIZED DNA")
        st.code(processed, language=None)
        st.success("DNA Refined. Pattern Uniformity: 0%")
    else:
        st.error("No input.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><center><p style='color:#1a1a1a; font-size:0.7rem;'>MEERUT LABS // PHANTOM-ULTRA 2026</p></center>", unsafe_allow_html=True)
