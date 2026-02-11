import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify Elite", page_icon="⚡", layout="centered")

# --- NEO-GLASS UI & NEON STYLING ---
st.markdown("""
    <style>
    /* Background with a deep space gradient */
    .stApp {
        background: radial-gradient(circle at top right, #1e1e2f, #0d0d15);
        color: #e0e0e0;
    }
    
    /* Glassmorphic Container */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        margin-bottom: 20px;
    }

    /* Neon Accents for Input & Buttons */
    textarea {
        background: rgba(0, 0, 0, 0.3) !important;
        color: #00f2ff !important;
        border: 1px solid #00f2ff33 !important;
        border-radius: 12px !important;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #7000ff, #00f2ff);
        border: none;
        color: white;
        padding: 15px 32px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 50px;
        box-shadow: 0px 0px 20px rgba(112, 0, 255, 0.4);
        transition: 0.4s;
    }
    
    .stButton>button:hover {
        box-shadow: 0px 0px 35px rgba(0, 242, 255, 0.6);
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE BYPASS ENGINE (Perplexity & Burstiness) ---
def elite_humanize(text):
    # Phase 1: Break AI 'Transition' Patterns
    replacements = {
        "furthermore": ["and honestly,", "also,", "on top of that,"],
        "moreover": ["plus,", "actually,", "another thing is,"],
        "consequently": ["so basically,", "as a result,"],
        "utilize": ["use", "go with", "work with"],
        "comprehensive": ["full-on", "detailed", "total"],
        "significant": ["major", "huge", "big-time"],
    }
    
    for word, options in replacements.items():
        text = re.sub(rf'\b{word}\b', random.choice(options), text, flags=re.IGNORECASE)

    # Phase 2: Inject Linguistic 'Burstiness'
    sentences = text.split(". ")
    new_sentences = []
    
    for i, s in enumerate(sentences):
        # AI writes mid-length sentences. Humans mix VERY short and long.
        if i % 4 == 0:
            new_sentences.append("It's worth noting.")
        
        # Add natural 'thought' particles
        fillers = ["I feel like ", "Basically, ", "Actually, ", ""]
        if len(s.split()) > 12: # Only on long 'robotic' sentences
            s = random.choice(fillers) + s[0].lower() + s[1:]
        
        new_sentences.append(s)
            
    return ". ".join(new_sentences)

# --- APP LAYOUT ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.title("⚡ SLANGIFY ELITE")
st.markdown("<p style='color:#00f2ff;'>0% AI Detection • Glass UI • High Perplexity Engine</p>", unsafe_allow_html=True)

input_text = st.text_area("Drop your AI text here:", height=200)

if st.button("BYPASS DETECTION 🛡️"):
    if input_text.strip():
        with st.spinner("Decoding AI patterns..."):
            time.sleep(1.5)
            # Apply the engine
            result = elite_humanize(input_text)
            
            st.markdown("### 🧬 Human-Optimized Output:")
            st.code(result, language=None)
            
            st.success("Human Rhythm Injected. Ready for Testing.")
    else:
        st.warning("Input is empty, captain.")
st.markdown('</div>', unsafe_allow_html=True)

# --- MONEY FOOTER ---
st.markdown("<br><center><p style='opacity:0.5;'>Built in the Lab. For the Students. 🎓</p></center>", unsafe_allow_html=True)
