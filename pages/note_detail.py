import streamlit as st
import os
from file_handle import *
import json
from generate_note import generate_note

### LOAD DATA ###
blackboard_file = st.session_state.blackboard_file
course_name = st.session_state.currentCourse
note_name = st.session_state.menu[st.session_state.menu[st.session_state.currentNodeIndex]]
syllabus_file = st.session_state.syllabusList[course_name]
audio_file = st.session_state.audio_file
personal_file = st.session_state.personal_file
note_name = "1" #for test purposes
note_path = f"../data/{course_name}/{note_name}"
if not os.path.exists(os.path.join(note_path, "note.md")):
    syllabus_content = read_syllabus(syllabus_file.name, course_name)
    blackboard_images = read_blackboard(blackboard_file.name, course_name, note_name)
    handnote_images = read_handnote(personal_file.name, course_name, note_name)
    audio_file_path = os.path.join(os.getcwd(), "data", course_name, note_name, audio_file.name)
    generate_note(blackboard_images, audio_file_path, handnote_images, context=syllabus_content, course_name=course_name, lecture_name=note_name)
with open(f"./data/{course_name}/{note_name}/questions.json", "r") as file:
    questions = json.load(file)
with open(f"./data/{course_name}/{note_name}/note.md", "r") as file:
    note = file.read()

st.session_state.note_text_raw=note

st.session_state.question_list=questions

st.set_page_config(page_title="Notebook Page", layout="wide")

st.title(note_name)

# Create columns for diagrams and questions
col1, col2 = st.columns([2, 1])

# LEFT COLUMN (Notebook content)
with col1:
    st.header("Notebook Content")
    if 'note_text_raw' in st.session_state:
        st.markdown(st.session_state.note_text_raw)
        #TODO: Add Diagrams picture inside the notes under appropiate section.
        # if 'diagram_list' in st.session_state:
        #     for diagram in st.session_state['diagram_list']:
        #         st.image(diagram['image_path'], caption=f"Diagram for {diagram['topic']}")
        #     else:
        #         st.info("No diagrams available.")
    else:
        st.write("No notes available. Please upload the markdown file.")

# RIGHT COLUMN (Diagrams and Questions)
with col2:
    st.header("Self-Quiz")

    # Display diagrams (images) if available


    # Display questions in tabs if available
    if 'question_list' in st.session_state:
        st.header("Interactive Questions")
        
        for question_data in st.session_state.question_list:
            topic = question_data['topic']
            st.subheader(f"Questions for {topic}")

            # Create tabs for Conceptual, Easy, and Challenging questions
            tab1, tab2, tab3 = st.tabs(["Conceptual", "Easy", "Challenging"])
            
            with tab1:
                for question in question_data['levels']:
                    if question['tag'] == "Conceptual":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_conceptual")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

            with tab2:
                for question in question_data['levels']:
                    if question['tag'] == "Easy":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_easy")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

            with tab3:
                for question in question_data['levels']:
                    if question['tag'] == "Challenging":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_challenging")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

    else:
        st.info("No questions available.")

# Footer
st.markdown("---")
st.metric(label="Progress", value="50%", delta="5%")

# Add some interactivity to stop the execution
if st.button("Stop the process"):
    st.stop()

st.success('Page Loaded Successfully!')



