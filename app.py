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
# CUSTOM UI STYLE
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Space+Grotesk:wght@300;500;700&display=swap');

.stApp {
    background-color: #0f0f0f;
    color: white;
}

.container-card {
    background: rgba(25,25,25,0.95);
    padding: 50px;
    border-radius: 20px;
    max-width: 900px;
    margin: auto;
    box-shadow: 0 0 40px rgba(0,0,0,0.6);
}

.logo {
    font-family: 'Syncopate', sans-serif;
    font-size: 3rem;
    text-align: center;
    background: linear-gradient(90deg, #00f2ff, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 0.9rem;
    letter-spacing: 3px;
    color: #00f2ff;
    margin-bottom: 30px;
}

textarea {
    font-family: 'Space Grotesk', sans-serif !important;
}

.stButton>button {
    border-radius: 40px;
    padding: 12px;
    font-weight: 600;
}

.footer-note {
    text-align: center;
    font-size: 0.8rem;
    opacity: 0.6;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# VOICE ENHANCEMENT ENGINE (LOCAL PROCESSING ONLY)
# --------------------------------------------------

def enhance_text(text, tone="Balanced", intensity=0.5, personal=False):
    if not text.strip():
        return ""

    # Synonym Enhancement Map
    synonyms = {
        "important": ["pivotal", "essential", "critical"],
        "big": ["major", "substantial", "significant"],
        "good": ["effective", "strong", "solid"],
        "bad": ["problematic", "inefficient", "weak"],
        "shows": ["demonstrates", "reveals", "illustrates"]
    }

    # Replace words based on intensity
    for word, options in synonyms.items():
        if random.random() < intensity:
            text = re.sub(
                rf"\b{word}\b",
                lambda _: random.choice(options),
                text,
                flags=re.IGNORECASE
            )

    # Sentence splitting
    sentences = re.split(r'(?<=[.!?])\s+', text)
    updated_sentences = []

    casual_starters = [
        "Honestly,",
        "The thing is,",
        "If you think about it,",
        "What stands out is,"
    ]

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        words = sentence.split()

        # Vary long sentences
        if len(words) > 20 and random.random() < intensity:
            mid = len(words) // 2
            sentence = " ".join(words[:mid]) + ". " + " ".join(words[mid:])

        # Casual tone modification
        if tone == "Casual" and random.random() < intensity:
            if len(sentence) > 2:
                sentence = random.choice(casual_starters) + " " + sentence[0].lower() + sentence[1:]

        updated_sentences.append(sentence)

    result = " ".join(updated_sentences)

    # Add personal intro
    if personal:
        intro = random.choice([
            "From my experience as a student,",
            "In my academic work, I have noticed that",
            "As someone studying this topic,"
        ])
        result = intro + " " + result

    # Clean spacing
    result = re.sub(r'\s+', ' ', result).strip()

    return result

# --------------------------------------------------
# UI LAYOUT
# --------------------------------------------------

st.markdown('<div class="container-card">', unsafe_allow_html=True)
st.markdown('<div class="logo">SLANGIFY</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI VOICE ENHANCEMENT TOOL</div>', unsafe_allow_html=True)

input_text = st.text_area(
    "Paste your draft below:",
    height=250,
    placeholder="Enter your assignment or draft here..."
)

col1, col2 = st.columns(2)

with col1:
    tone = st.selectbox("Select Tone", ["Balanced", "Casual"])

with col2:
    intensity = st.slider(
        "Enhancement Intensity",
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        step=0.1
    )

personal_option = st.checkbox("Add Personal Perspective")

# --------------------------------------------------
# PROCESS BUTTON
# --------------------------------------------------

if st.button("Enhance Writing"):
    if input_text:
        with st.spinner("Enhancing your writing..."):
            time.sleep(1)
            output_text = enhance_text(
                input_text,
                tone=tone,
                intensity=intensity,
                personal=personal_option
            )

        st.markdown("### ✨ Enhanced Output")
        st.text_area("", output_text, height=250)

        # Word count
        word_count = len(output_text.split())
        st.info(f"Word Count: {word_count}")

        # Download option
        st.download_button(
            label="Download as .txt",
            data=output_text,
            file_name="slangify_output.txt",
            mime="text/plain"
        )

        st.success("Enhancement complete.")
    else:
        st.error("Please paste text first.")

# Privacy Notice
st.markdown(
    '<div class="footer-note">🔒 Privacy Notice: This app does not store, save, or share your text. All processing happens temporarily during your session.</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
