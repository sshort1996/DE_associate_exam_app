import streamlit as st
import json

# Read the questions from the json file
with open("questions.json") as f:
    questions = json.load(f)

# Initialize counters for correct and incorrect answers
session_vars = {
    'correct_count': 0,
    'incorrect_count': 0,
    'attempted': []
}

for key, var in session_vars.items():
    if key not in st.session_state:
        st.session_state[key] = var

# Iterate over each question
for i, question in enumerate(questions):
    
    if question['question'] is not None:
        st.title(f"Question {i}")

        # Check if the question has been attempted
        if i in [index for _, index in st.session_state['attempted']]:
            # Apply grey color using HTML/CSS
            st.markdown(
                f"<style>.question-{i} {{ color: grey; }}</style>",
                unsafe_allow_html=True
            )
        
        # Grey out submit button and radio button if the question has been attempted
        if i in [index for _, index in st.session_state['attempted']]:
            button_text = "Question Attempted"
            button_disabled = True
            radio_disabled = True
        else:
            button_text = f'Submit#{i}'
            button_disabled = False
            radio_disabled = False

        st.write(question['question'])
        
        # Show multiple choices as radio buttons
        selected_choice = st.radio("Select your answer:", options=question['choices'], disabled=radio_disabled, key=f"radio_{i}")
        
        # Check if the selected choice is correct or incorrect
        if st.button(button_text, key=f"submit_{i}", disabled=button_disabled):
            if selected_choice == question['answer']:
                st.write("You chose correctly!")
                st.session_state['correct_count'] += 1
            else:
                st.write("You chose incorrectly!")
                st.session_state['incorrect_count'] += 1

            st.session_state['attempted'].append((selected_choice, i))
            st.write(f"Correct count: {st.session_state['correct_count']}, Incorrect count: {st.session_state['incorrect_count']}")
            st.write(f"{st.session_state['correct_count']}/{st.session_state['incorrect_count']+st.session_state['correct_count']}")
                

# Summary section
st.title("Summary")
st.write("Here are the incorrect questions and their answers:")

# Iterate over attempted questions to find incorrect ones
for selected_choice, question_index in st.session_state['attempted']:
    question = questions[question_index]
    if selected_choice != question['answer']:
        st.write(f"- Question: {question['question']}  \n  Your answer: {selected_choice}   \n  Correct answer: {question['answer']}")
