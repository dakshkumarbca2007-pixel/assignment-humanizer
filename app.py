import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Phantom-X", page_icon="🌑", layout="wide")

# --- HIGH-TECH OBSIDIAN CHROME UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@300;500;700&display=swap');

    .stApp {
        background: #000000;
        color: #ffffff;
    }

    /* Premium High-Tech Card */
    .phantom-card {
        background: rgba(15, 15, 15, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 30px;
        padding: 50px;
        max-width: 850px;
        margin: auto;
        position: relative;
        box-shadow: 0 0 50px rgba(0,0,0,1);
        overflow: hidden;
    }

    /* Vector Wave Animation */
    .phantom-card::before {
        content: "";
        position: absolute;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: conic-gradient(from 180deg, transparent, #00f2ff, transparent 40%);
        animation: rotate 6s linear infinite;
        z-index: -1;
        opacity: 0.1;
    }

    @keyframes rotate { 100% { transform: rotate(1turn); } }

    /* Chrome Brutalist Logo */
    .phantom-logo {
        font-family: 'Syncopate', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #333 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -6px;
        margin-bottom: 5px;
    }

    /* Premium Input Void */
    .stTextArea textarea {
        background: #050505 !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 15px !important;
        color: #00f2ff !important;
        font-family: 'Space Grotesk', sans-serif !important;
        padding: 25px !important;
        font-size: 1.1rem !important;
    }

    /* Liquid Mercury Button */
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
        letter-spacing: 3px;
        transition: 0.5s cubic-bezier(0.19, 1, 0.22, 1);
    }

    .stButton>button:hover {
        background: #00f2ff;
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 242, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ADVANCED BYPASS ENGINE (PHANTOM-CORE) ---
def phantom_scrambler(text):
    # Phase 1: Break Predictability (Injecting "Human Errors" & Hedging)
    replacements = {
        "furthermore": ["and honestly,", "also,"],
        "consequently": ["so basically,", "which means"],
        "significant": ["huge", "massive"],
        "essential": ["key", "a big deal"],
        "demonstrates": ["shows", "really proves"]
    }
    
    for word, options in replacements.items():
        text = re.sub(rf'\b{word}\b', random.choice(options), text, flags=re.IGNORECASE)

    # Phase 2: Structural Jitter (Non-Linear Rhythm)
    sentences = text.split(". ")
    scrambled = []
    
    for i, s in enumerate(sentences):
        # AI never starts sentences with 'Actually' or 'I mean'
        if i % 3 == 0:
            s = random.choice(["I mean, ", "Actually, ", "Basically, ", "So, "]) + s[0].lower() + s[1:]
        
        # Inject "Thought Markers" (Dashes and Ellipses)
        if len(s.split()) > 10 and random.random() > 0.6:
            words = s.split()
            mid = len(words) // 2
            s = " ".join(words[:mid]) + "—" + " ".join(words[mid:])
            
        scrambled.append(s)

    # Phase 3: The "Deep Stealth" Injection (Hardcoded Pattern Killer)
    # Adding a personalized student opening
    scrambled.insert(0, "From a student perspective,")
    
    # Phase 4: Intentional Linguistic Flaws (Removing double spaces/fixing bot-spacing)
    result = ". ".join(scrambled).strip()
    result = result.replace("..", ".").replace(" ,", ",")
    
    return result

# --- INTERFACE ---
st.markdown('<div class="phantom-card">', unsafe_allow_html=True)
st.markdown('<h1 class="phantom-logo">SLANGIFY</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00f2ff; letter-spacing:10px; font-size:0.6rem; opacity:0.6;">NEURAL BYPASS ACTIVE // PROTOCOL 10.0</p>', unsafe_allow_html=True)

user_text = st.text_area("", height=250, placeholder="SYSTEM READY. PASTE DNA...")

if st.button("EXECUTE GHOST MODE"):
    if user_text:
        with st.status("Breaking Pattern Matrices...", expanded=False):
            time.sleep(2)
            processed = phantom_scrambler(user_text)
        
        st.markdown("### 🧬 SCRAMBLED OUTPUT")
        st.code(processed, language=None)
        st.success("DNA Scrambled. Pattern Uniformity: 0%")
    else:
        st.error("Input missing.")
st.markdown('</div>', unsafe_allow_html=True)
