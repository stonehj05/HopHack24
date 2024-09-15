import streamlit as st
import os
from file_handle import *
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
os.makedirs("data", exist_ok=True)
os.makedirs(f"data/{course_name}", exist_ok=True)
os.makedirs(f"data/{course_name}/1", exist_ok=True)
with open(os.path.join(os.getcwd(), "data", course_name, syllabus_file.name), "wb") as file:
    file.write(syllabus_file.getbuffer())
with open(os.path.join(os.getcwd(), "data", course_name, "1", blackboard_file.name), "wb") as file: #1 is a placeholder now
    file.write(blackboard_file.getbuffer())
with open(os.path.join(os.getcwd(), "data", course_name, "1", audio_file.name), "wb") as file: #1 is a placeholder now
    file.write(audio_file.getbuffer())
with open(os.path.join(os.getcwd(), "data", course_name, "1", personal_file.name), "wb") as file: #1 is a placeholder now
    file.write(personal_file.getbuffer())