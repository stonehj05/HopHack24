import streamlit as st
from pages import page1

# Initialize session state variables if they don't exist
for i in range(1, 6):
    if f'{i}thCourseNotebookCount' not in st.session_state:
        st.session_state[f'{i}thCourseNotebookCount'] = 0

# Initialize session state for syllabus and course name
if 'syllabus' not in st.session_state:
    st.session_state['syllabus'] = None

if 'CourseName' not in st.session_state:
    st.session_state['CourseName'] = ""

# Set page config
st.set_page_config(page_title="AI Notetaker", page_icon="📝", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .title {
        font-family: "Times New Roman", Times, serif;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }
    .description {
        font-family: "Times New Roman", Times, serif;
        font-size: 20px;
        text-align: center;
        margin: 10px;
    }
    .section-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 30px;
        text-align: left;
        margin: 20px 0 10px 0;
    }
    .course-link {
        font-size: 24px;
        font-weight: bold;
        color: #3498db;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state to keep track of pages
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Define the main page content (this will be the default landing page)
def main_page():
    st.markdown('<div class="title">AI Notetaker</div>', unsafe_allow_html=True)

    description_text = """
    Our AI-powered note-taking application transforms the educational experience by automating the capture of lecture content, benefiting all students, especially those with ADHD, visual or hearing impairments, and mental health challenges. The platform allows students to engage more actively in lectures without the distraction of manual note-taking.
    """
    st.markdown(f'<div class="description">{description_text}</div>', unsafe_allow_html=True)

    # Syllabus file uploader
    st.markdown('<div class="description">Please enter the new course syllabus to start: 📂</div>', unsafe_allow_html=True)
    syllabus = st.file_uploader("", type=['pdf', 'docx', 'txt'])

    if syllabus is not None:
        st.session_state['syllabus'] = syllabus

    # Text input for course name
    course_name = st.text_input("Enter Course Name", value=st.session_state['CourseName'], placeholder="Enter course name here")
    if course_name:
        st.session_state['CourseName'] = course_name

    # Conditionally display the button to go to Page 1 only if both the syllabus is uploaded and the course name is entered
    if st.session_state['syllabus'] is not None and st.session_state['CourseName']:
        st.markdown('<div class="description">Syllabus uploaded and course name provided!</div>', unsafe_allow_html=True)

        # Use the course name as the button label
        button_label = f'Go to {course_name}' if course_name else 'Go to Page 1'

        if st.button(button_label):
            st.session_state.page = 'page1'
            st.rerun()  # Reload the app to switch to page 1

# Dynamically show content based on the current page
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'page1':
    page1()