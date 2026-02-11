import streamlit as st
import random
import re
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Slangify – Voice Enhancer",
    page_icon="✨",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM UI STYLE (Clean Premium Dark)
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@300;500;700&display=swap');

.stApp {
    background: #0e0e0e;
    color: white;
}

.main-card {
    background: rgba(20,20,20,0.9);
    padding: 50px;
    border-radius: 25px;
    max-width: 900px;
    margin: auto;
    box-shadow: 0 0 40px rgba(0,0,0,0.6);
}

.logo {
    font-family: 'Syncopate', sans-serif;
    font-size: 3.5rem;
    text-align: center;
    background: linear-gradient(90deg, #00f2ff, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtext {
    text-align:center;
    color:#00f2ff;
    font-size:0.8rem;
    letter-spacing:3px;
    margin-bottom:40px;
}

.stButton>button {
    border-radius: 50px;
    padding: 15px;
    font-weight: 600;
}

textarea {
    font-family: 'Space Grotesk', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# VOICE ENHANCEMENT ENGINE
# --------------------------------------------------

def enhance_voice(text, tone="Balanced", intensity=0.5, add_personal=False):
    if not text.strip():
        return ""

    # --- Synonym Enhancement ---
    synonym_map = {
        "important": ["pivotal", "critical", "essential"],
        "big": ["substantial", "major", "significant"],
        "good": ["effective", "strong", "solid"],
        "bad": ["problematic", "weak", "inefficient"],
        "shows": ["demonstrates", "reveals", "illustrates"],
    }

    for word, options in synonym_map.items():
        if random.random() < intensity:
            text = re.sub(
                rf"\b{word}\b",
                lambda _: random.choice(options),
                text,
                flags=re.IGNORECASE
            )

    # --- Sentence Splitting ---
    sentences = re.split(r'(?<=[.!?])\s+', text)
    improved = []

    conversational_openers = [
        "Honestly,",
        "The thing is,",
        "If you think about it,",
        "What stands out is,"
    ]

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        words = s.split()

        # Rhythm variation
        if len(words) > 18 and random.random() < intensity:
            mid = len(words) // 2
            s = " ".join(words[:mid]) + ". " + " ".join(words[mid:])

        # Tone adjustment
        if tone == "Casual" and random.random() < intensity:
            s = f"{random.choice(conversational_openers)} {s[0].lower() + s[1:] if len(s)>1 else s}"

        improved.append(s)

    result = " ".join(improved)

    # Personal perspective option
    if add_personal:
        intro = random.choice([
            "From my experience as a student,",
            "In my academic work, I've noticed that",
            "As someone studying this topic,"
        ])
        result = f"{intro} {result}"

    result = re.sub(r'\s+', ' ', result).strip()

    return result


# --------------------------------------------------
# UI LAYOUT
# --------------------------------------------------

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="logo">SLANGIFY</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">AI VOICE REFINEMENT ENGINE</div>', unsafe_allow_html=True)

user_text = st.text_area(
    "Paste your draft below:",
    height=250,
    placeholder="Enter your text here..."
)

col1, col2 = st.columns(2)

with col1:
    tone_option = st.selectbox(
        "Select Tone",
        ["Balanced", "Casual"]
    )

with col2:
    intensity = st.slider(
        "Enhancement Intensity",
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        step=0.1
    )

add_personal = st.checkbox("Add Personal Perspective")

# --------------------------------------------------
# PROCESS BUTTON
# --------------------------------------------------

if st.button("Enhance Writing"):
    if user_text:
        with st.spinner("Refining voice and flow..."):
            time.sleep(1.2)
            processed = enhance_voice(
                user_text,
                tone=tone_option,
                intensity=intensity,
                add_personal=add_personal
            )

        st.markdown("### ✨ Enhanced Output")
        st.text_area("", processed, height=250)

        st.download_button(
            label="Download as .txt",
            data=processed,
            file_name="slangify_output.txt",
            mime="text/plain"
        )

        st.success("Enhancement complete.")
    else:
        st.error("Please enter text first.")

st.markdown('</div>', unsafe_allow_html=True)
