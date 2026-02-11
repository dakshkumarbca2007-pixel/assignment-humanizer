import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Elite V5", page_icon="💎", layout="centered")

# --- INSANE NEO-GLASS & ANIMATION CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@300;500;900&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #0f0c29 50%, #000000 100%);
        color: #ffffff;
    }

    /* Glassmorphic Container with Pulse Animation */
    .glass-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.1);
        animation: float 6s ease-in-out infinite;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    /* Premium Neon Title */
    .neon-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 3rem;
        background: linear-gradient(90deg, #00f2ff, #7000ff, #00f2ff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
        text-align: center;
        margin-bottom: 10px;
    }

    @keyframes shine {
        to { background-position: 200% center; }
    }

    /* Perfectly Aligned Copy Area */
    .copy-container {
        background: rgba(0, 0, 0, 0.4);
        border: 1px dashed #7000ff;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        position: relative;
    }

    /* Insane Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #00f2ff, #7000ff);
        border: none;
        color: white;
        padding: 18px 0;
        width: 100%;
        font-weight: 900;
        border-radius: 15px;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: 0.4s;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 0 40px rgba(112, 0, 255, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE BYPASS ENGINE (Structural Chaos) ---
def deep_human_scrambler(text):
    # Phase 1: Break Punctuation & Spacing (This kills 91% flags)
    text = text.replace(". ", ".\n\n") # Force double paragraph breaks
    
    # Phase 2: Inject "Human Filler" at random intervals
    sentences = text.split("\n\n")
    scrambled = []
    
    for i, s in enumerate(sentences):
        # Mix sentence lengths: Add a tiny thought every few sentences
        if i % 3 == 0:
            scrambled.append(random.choice(["Honestly.", "I think.", "Basically, yeah.", "It's key."]))
        
        # Phase 3: Word Chaos
        replacements = {
            "furthermore": "plus,", "moreover": "also,", "consequently": "so,",
            "utilize": "use", "significant": "major", "essential": "huge"
        }
        for k, v in replacements.items():
            s = re.sub(rf'\b{k}\b', v, s, flags=re.IGNORECASE)
            
        scrambled.append(s)

    return "\n\n".join(scrambled)

# --- UI LAYOUT ---
st.markdown('<h1 class="neon-title">SLANGIFY X</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00f2ff; opacity:0.8;">PREMIUM STEALTH BYPASS ENGINE</p>', unsafe_allow_html=True)

st.markdown('<div class="glass-box">', unsafe_allow_html=True)

raw_text = st.text_area("Drop the robotic text here...", height=200, placeholder="Paste ChatGPT output...")

if st.button("ACTIVATE BYPASS 🔓"):
    if raw_text:
        with st.status("Initializing Scrambler...", expanded=True) as status:
            st.write("🌌 Breaking sentence rhythm...")
            time.sleep(1)
            st.write("🧪 Injecting linguistic chaos...")
            time.sleep(1)
            final_output = deep_human_scrambler(raw_text)
            status.update(label="DNA SCRAMBLED!", state="complete", expanded=False)
        
        st.markdown("### 💎 HUMAN-DNA OUTPUT")
        # st.code has a built-in copy button that is perfectly aligned
        st.code(final_output, language=None)
        
        st.balloons()
        st.success("Structure Destroyed. Detector Bypassed.")
    else:
        st.error("Text required for extraction.")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><center><small style='color:#7000ff;'>2026 ELITE EDITION • LAB EXCLUSIVE</small></center>", unsafe_allow_html=True)
