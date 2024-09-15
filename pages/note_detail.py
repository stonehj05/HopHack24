import streamlit as st
import os
from file_handle import *
from generate_note import generate_note
# Set page configuration
st.write(page_title="Notebook Page", layout="wide")

# Initialize session state for notebook name if not already set
if 'notebookName' not in st.session_state or st.session_state['notebookName'] is None:
    st.session_state['notebookName'] = "Notebook Title"  # Set a default title if not set

# Title stored in session state
st.title(st.session_state['notebookName'])

# CSS to style the return button in the top right corner
st.markdown(
    """
    <style>
    .return-button {
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a button that links back to page 1
st.page_link("./pages/course_page.py", label="Return to Course Page", icon="🏠")
# st.markdown('<a href="/page1" class="return-button">Return to Page 1</a>', unsafe_allow_html=True)

# Example content in the notebook page
st.write("This is the content of your notebook.")

#st.session_state.audio_file
#st.session_state.blackboard_file
#st.session_state.personal_file
blackboard_file = st.session_state.blackboard_file
course_name = st.session_state.courseDictionary[1]
syllabus_file = st.session_state.syllabusList[course_name]
audio_file = st.session_state.audio_file
personal_file = st.session_state.personal_file
note_name = "1" #for test purposes
note_path = f"../data/{course_name}/{note_name}"
if not os.path.exists(os.path.join(note_path, "note.md")):
    syllabus_content = read_syllabus(syllabus_file.name, course_name)
    blackboard_images = read_blackboard(blackboard_file.name, course_name, note_name)
    handnote_images = read_handnote(personal_file.name, course_name, note_name)
    audio_file_path = os.path.join(os.getcwd(), "data", course_name, "1", audio_file.name)
    generate_note(blackboard_images, audio_file_path, handnote_images, context=syllabus_content, course_name=course_name, lecture_name=note_name) 
pass #replace this with illustration function based on markdown
