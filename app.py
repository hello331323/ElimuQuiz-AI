import streamlit as st
from openai import OpenAI

# 1. Setup the Web Interface
st.title("🎓 StudyBridge: Teacher's Mastery Generator")
st.subheader("Create a 50-question exam in seconds")

# Sidebar for Settings
with st.sidebar:
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    grade_level = st.selectbox("Grade Level", ["Elementary", "Middle School", "High School", "University"])
    difficulty = st.select_slider("Difficulty", options=["Easy", "Standard", "Challenging"])

# Main Input
topic = st.text_input("Enter the Exam Topic (e.g., Photosynthesis, Roman Empire)")
num_questions = st.slider("Number of Questions", min_value=1, max_value=50, value=10)

if st.button("✨ Generate Exam"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar!")
    else:
        client = OpenAI(api_key=api_key)
        
        with st.spinner("AI is drafting your exam..."):
            # The Prompt - This tells the AI exactly how to behave
            prompt = f"""
            Create a {num_questions} question exam for {grade_level} students on the topic of '{topic}'.
            The difficulty should be {difficulty}. 
            Structure the exam with Multiple Choice and Short Answer.
            Provide a clear Answer Key at the very end.
            """

            # Call the AI
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Display the result
            exam_text = response.choices[0].message.content
            st.markdown("---")
            st.markdown(exam_text)
            
            # Allow teacher to download it
            st.download_button("Download Exam as Text", exam_text)
