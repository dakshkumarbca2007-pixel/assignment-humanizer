import streamlit as st

st.set_page_config(page_title="Slangify AI", page_icon="📝")

# Your humanizing logic
human_map = {
    "furthermore": "also", "moreover": "plus", "consequently": "so",
    "utilize": "use", "comprehensive": "full", "exhibit": "show",
    "delve into": "look at", "testament": "proof", "essential": "key"
}

st.title("🎓 Slangify AI: Student Humanizer")
st.write("Paste your robotic AI text below to make it sound like a real student.")

user_input = st.text_area("Input AI Text:", height=200)

if st.button("Humanize ✨"):
    if user_input:
        output = user_input
        for ai_word, student_word in human_map.items():
            output = output.replace(ai_word, student_word)
            output = output.replace(ai_word.capitalize(), student_word.capitalize())
        
        st.subheader("Humanized Result:")
        st.success(output)
        
        st.divider()
        st.write("🙏 Saved your grade? Support the dev!")
        # Replace 'yourusername' with your actual BuyMeACoffee link later
        st.link_button("☕ Buy Me a Coffee ($1)", "https://www.buymeacoffee.com")
    else:
        st.error("Please paste text first!")
