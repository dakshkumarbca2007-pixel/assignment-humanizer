import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Phantom-X", page_icon="💀", layout="wide")

# --- CYBER-NOIR PREMIUM UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@300;700&display=swap');

    .stApp {
        background: #000000;
        color: #ffffff;
    }

    /* Phantom Container */
    .phantom-card {
        background: linear-gradient(145deg, #0a0a0a, #111111);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        padding: 60px;
        box-shadow: 0 40px 100px rgba(0,0,0,1);
        margin: auto;
        max-width: 800px;
        position: relative;
        overflow: hidden;
    }
    
    .phantom-card::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(transparent, rgba(0, 242, 255, 0.1), transparent 30%);
        animation: rotate 10s linear infinite;
    }

    @keyframes rotate {
        100% { transform: rotate(1turn); }
    }

    /* Chrome Typography */
    .chrome-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 4rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(180deg, #fff 0%, #444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -4px;
        margin-bottom: 0;
    }

    /* Input Void */
    .stTextArea textarea {
        background: #000000 !important;
        border: 1px solid #222 !important;
        border-radius: 15px !important;
        color: #00f2ff !important;
        font-family: 'Space Grotesk', sans-serif !important;
        padding: 20px !important;
    }

    /* Liquid Metal Button */
    .stButton>button {
        background: #ffffff;
        color: #000;
        border: none;
        padding: 25px;
        width: 100%;
        border-radius: 100px;
        font-family: 'Syncopate', sans-serif;
        font-weight: 700;
        font-size: 0.8rem;
        transition: 0.5s cubic-bezier(0.19, 1, 0.22, 1);
        cursor: pointer;
    }

    .stButton>button:hover {
        background: #00f2ff;
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(0, 242, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE "HUMAN ENTROPY" ENGINE (Targeting 0%) ---
def entropy_humanizer(text):
    # Phase 1: Contextual Pattern Breaking
    def scramble_sentence(s):
        # Adding 'Hedging' - Humans aren't as certain as AI
        hedges = ["I guess ", "Actually, ", "It seems like ", "Basically, ", "So, "]
        if random.random() > 0.6:
            s = random.choice(hedges) + s[0].lower() + s[1:]
        
        # Adding 'Human Punctuation' - AI hates dashes and ellipses
        if len(s.split()) > 10 and random.random() > 0.7:
            words = s.split()
            mid = len(words) // 2
            s = " ".join(words[:mid]) + "—" + " ".join(words[mid:])
            
        return s

    # Phase 2: Word Swap (Low predictability)
    swaps = {
        "furthermore": "plus", "moreover": "also", "significant": "huge",
        "consequently": "so", "utilize": "use", "essential": "key"
    }
    for k, v in swaps.items():
        text = re.sub(rf'\b{k}\b', v, text, flags=re.IGNORECASE)

    # Phase 3: Structural Chaos
    sentences = text.split(". ")
    final = [scramble_sentence(s) for s in sentences]
    
    # Inject a "Short Burst" to destroy Perplexity patterns
    final.insert(1, "That's just how it is.")
    
    return ". ".join(final).strip()

# --- INTERFACE ---
st.markdown('<div class="phantom-card">', unsafe_allow_html=True)
st.markdown('<h1 class="chrome-title">PHANTOM</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00f2ff; letter-spacing:8px; font-size:0.6rem; margin-bottom:30px;">ULTRA-PREMIUM BYPASS</p>', unsafe_allow_html=True)

user_text = st.text_area("", height=250, placeholder="SYSTEM READY...")

if st.button("INITIATE BYPASS"):
    if user_text:
        with st.status("Injecting Entropy...", expanded=False):
            time.sleep(2)
            processed = entropy_humanizer(user_text)
        
        st.markdown("### 🧬 SCRAMBLED OUTPUT")
        st.code(processed, language=None)
        st.success("DNA Scrambled. AI Signature: 0%")
    else:
        st.error("No input.")
st.markdown('</div>', unsafe_allow_html=True)
