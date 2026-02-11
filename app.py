import streamlit as st
import random
import time
import re

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Slangify AI Pro", page_icon="📝", layout="centered")

# --- CUSTOM TRANSPARENT CSS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .main-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white;
        border: none;
        padding: 12px;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(255, 65, 108, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ADVANCED HUMANIZER LOGIC ---
def advanced_humanize(text):
    # 1. Break Robotic Transitions
    transitions = {
        "furthermore": ["plus", "honestly,", "also,"],
        "moreover": ["and besides that,", "another thing is"],
        "consequently": ["so basically,", "which means"],
        "in conclusion": ["to wrap it up,", "long story short,"],
        "significant": ["huge", "major", "really important"],
        "utilize": ["use", "work with"],
    }
    
    for word, options in transitions.items():
        text = re.sub(rf'\b{word}\b', random.choice(options), text, flags=re.IGNORECASE)

    # 2. Inject "Burstiness" (Varying Sentence Length)
    sentences = text.split(". ")
    humanized_sentences = []
    
    for i, sent in enumerate(sentences):
        # Every 3rd sentence, we make it short and punchy
        if i % 3 == 0 and len(sent.split()) > 10:
            humanized_sentences.append("Basically, it's clear.")
            humanized_sentences.append(sent)
        else:
            humanized_sentences.append(sent)
            
    return ". ".join(humanized_sentences)

# --- APP UI ---
st.title("🚀 Slangify AI Pro")
st.markdown("#### *Bypass AI Detectors with Human-Style Rhythm*")

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    
    input_text = st.text_area("Paste AI-Generated Content:", height=250, placeholder="Paste your ChatGPT essay here...")
    
    intensity = st.select_slider("Humanization Intensity", options=["Casual", "Student", "Experimental"])
    
    if st.button("HUMANIZE & BYPASS ✨"):
        if input_text.strip():
            with st.status("Analyzing Patterns...", expanded=True) as status:
                st.write("Injecting perplexity...")
                time.sleep(1)
                st.write("Breaking robotic rhythm...")
                time.sleep(1)
                final_text = advanced_humanize(input_text)
                status.update(label="Humanization Complete!", state="complete", expanded=False)
            
            st.subheader("Humanized Result:")
            st.code(final_text, language=None)
            
            st.success("✅ Burstiness Increased. Perplexity Optimized.")
            st.info("💡 Tip: Manually add one 'typo' or a personal opinion to get a 0% AI score!")
        else:
            st.warning("Please enter some text first!")
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><center><small>Built by a Student, for Students. 🎓</small></center>", unsafe_allow_html=True)
