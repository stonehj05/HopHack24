import streamlit as st

from pages import page1

# Initialize session state variables if they don't exist
if 'firstCourseNotebookCount' not in st.session_state:
    st.session_state.firstCourseNotebookCount = 0

if 'secondCourseNotebookCount' not in st.session_state:
    st.session_state.secondCourseNotebookCount = 0

if 'thirdCourseNotebookCount' not in st.session_state:
    st.session_state.thirdCourseNotebookCount = 0

if 'fourthCourseNotebookCount' not in st.session_state:
    st.session_state.fourthCourseNotebookCount = 0

if 'fifthCourseNotebookCount' not in st.session_state:
    st.session_state.fifthCourseNotebookCount = 0

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

    # Text input for notebook name
    notebook_name = st.text_input("Enter Notebook Name", value="", placeholder="Enter notebook name here")
    if notebook_name:
        st.session_state['notebookName'] = notebook_name

    # Conditionally display the button to go to Page 1 only if both the syllabus is uploaded and the notebook name is entered
    if 'syllabus' in st.session_state and 'notebookName' in st.session_state:
        st.markdown('<div class="description">Syllabus uploaded and notebook name provided!</div>', unsafe_allow_html=True)

        # Show button to navigate to Page 1 only after inputs are given
        if st.button('Go to Introductory Chemistry I'):
            st.session_state.page = 'page1'
            st.rerun()  # Reload the app to switch to page 1

# Dynamically show content based on the current page
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'page1':
    page1()
