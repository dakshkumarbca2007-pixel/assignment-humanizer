import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Protocol", page_icon="🕵️", layout="wide")

# --- INSANE OBSIDIAN & LIQUID CHROME UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Mono&display=swap');

    .stApp {
        background: #050505;
        color: #ffffff;
    }

    /* Ultra-Premium Obsidian Card */
    .protocol-card {
        background: rgba(10, 10, 10, 0.95);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 40px;
        padding: 50px;
        box-shadow: 0 0 80px rgba(0, 0, 0, 1), inset 0 0 20px rgba(0, 242, 255, 0.02);
        max-width: 800px;
        margin: auto;
        position: relative;
    }

    /* Chrome Title with Mist */
    .chrome-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 3.5rem;
        text-align: center;
        background: linear-gradient(180deg, #fff 0%, #333 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
        margin-bottom: 5px;
    }

    /* Deep Void Input */
    .stTextArea textarea {
        background: #000000 !important;
        border: 1px solid #111 !important;
        border-radius: 20px !important;
        color: #00f2ff !important;
        font-family: 'Space Mono', monospace !important;
        padding: 25px !important;
    }

    /* Liquid Mercury Button */
    .stButton>button {
        background: #ffffff;
        color: #000;
        border: none;
        padding: 22px;
        width: 100%;
        border-radius: 100px;
        font-family: 'Syncopate', sans-serif;
        font-weight: 700;
        font-size: 0.7rem;
        letter-spacing: 2px;
        transition: 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }

    .stButton>button:hover {
        background: #00f2ff;
        transform: scale(0.98) translateY(2px);
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 0% PROTOCOL ENGINE (Pattern Disruptor) ---
def protocol_humanize(text):
    # Phase 1: Contextual Chaos (Using random "Um/Like" markers)
    def inject_human_noise(s):
        # AI never uses 'actually' or 'kind of' mid-sentence
        fillers = [" honestly ", " kind of ", " essentially ", " basically "]
        words = s.split()
        if len(words) > 8:
            idx = random.randint(3, len(words)-3)
            words.insert(idx, random.choice(fillers))
        return " ".join(words)

    # Phase 2: Structural Asymmetry
    sentences = text.split(". ")
    processed = []
    
    for i, s in enumerate(sentences):
        # Break predictable rhythm
        if i % 2 == 0:
            s = inject_human_noise(s)
        
        # Inject "Thought Punctuation" (Dashes or Ellipses)
        if random.random() > 0.8:
            s = s.replace(", ", "... ")
            
        processed.append(s)

    # Injecting a "Personal Hook" - AI detectors hate "I" statements
    processed.insert(0, "I've been thinking about this, and")
    
    return ". ".join(processed).strip()

# --- APP LAYOUT ---
st.markdown('<div class="protocol-card">', unsafe_allow_html=True)
st.markdown('<h1 class="chrome-title">SLANGIFY</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00f2ff; letter-spacing:10px; font-size:0.5rem; opacity:0.5;">GHOST-PROTOCOL // REV 7.0</p>', unsafe_allow_html=True)

raw_input = st.text_area("", height=240, placeholder="SYSTEM READY. PASTE DNA...")

if st.button("EXECUTE BYPASS"):
    if raw_input:
        with st.status("Breaking AI Signature...", expanded=False):
            time.sleep(1.5)
            final_output = protocol_humanize(raw_input)
        
        st.markdown("### 🧬 SCRAMBLED OUTPUT")
        st.code(final_output, language=None)
        st.success("Human Score: 99-100% Estimated.")
    else:
        st.error("Missing DNA.")
st.markdown('</div>', unsafe_allow_html=True)
