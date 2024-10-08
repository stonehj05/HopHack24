import streamlit as st
from picture import *
import copy

#A int that keep track the current index of note, which correspond to the order that they are added in their course
# if 'noteIndex' not in st.session_state:
#     st.session_state.noteIndex = 0
if st.session_state.currentCourse in st.session_state.menu and st.session_state.noteupdateCheck:
    noteDictionary = st.session_state.menu[st.session_state.currentCourse]
    noteIndex = len(noteDictionary)
elif st.session_state.currentCourse not in st.session_state.menu and st.session_state.noteupdateCheck:
    noteDictionary = {}
    noteIndex = 0

# Custom CSS to position the title and button on the same line
st.markdown("""
    <style>
    .title-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    .title {
        font-family: "Times New Roman", Times, serif;
        font-size: 50px;
        font-weight: bold;
        align-items: center;
    }
    .button-container {
        margin-left: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the title and the button on the same line
col1, col2 = st.columns([4, 1])  # Adjust the proportions (4:1) for spacing

with col1:
    st.markdown(f'<div class="title">{st.session_state.currentCourse}</div>', unsafe_allow_html=True)

with col2:
    if st.button('Go back to homepage'):
        st.switch_page('main.py')
    if st.button('Go back to HelpBot'):
        st.switch_page('pages/chatbox.py')

# Ensure there is a valid course index
if st.session_state.courseIndex == 0:
    st.error("No course selected.")
    st.switch_page('main.py')

# Get the most recent course index and course name
course_name = st.session_state.currentCourse  # Get the course name based on the index
syllabus = st.session_state.syllabusList.get(1, "No syllabus available")

# # Display the course summary or syllabus
# summary = "This course introduces students to the fundamentals of chemistry, including atomic structure, periodic trends, and chemical reactions."
# st.markdown('<div class="text-content">' + summary + '</div>', unsafe_allow_html=True)

# Display images of folders with note names underneath
if st.session_state.noteupdateCheck:
    if noteIndex > 0:
        # note_image_display("Notebook.png", noteIndex, noteDictionary)
        note_image_display('notebook.PNG', noteIndex, noteDictionary)
    else:
        st.markdown('<p class="input-title">Please create a new notebook to start</p>', unsafe_allow_html=True)

# Add a blank space before the text input field
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Create a new notebook text input with a large font
st.markdown('<div class="larger-text">Create a new notebook by entering its name:</div>', unsafe_allow_html=True)
noteName = st.text_input("", value="", placeholder="Enter Notebook Name Here")

if noteName:
    if st.session_state.noteupdateCheck:
        st.session_state.noteupdateCheck = False
        st.session_state.currentNoteIndex = noteIndex + 1
        noteDictionary[st.session_state.currentNoteIndex] = noteName
        st.session_state.menu[st.session_state.currentCourse] = copy.deepcopy(noteDictionary)
        st.write("Notebook Created Successfully")
        # Handle the creation of a new notebook
        if st.button('Upload More Information'):
            st.session_state.currentNoteIndex += 1
            st.switch_page('./pages/upload_new_note.py')
    else:
        st.write("Notebook Created Successfully")
        if st.button('Upload More Information'):
            st.switch_page('./pages/upload_new_note.py')