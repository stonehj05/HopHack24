import streamlit as st

# Set the page configuration
st.set_page_config(page_title="AI Notetaker", page_icon="📝")

# Custom CSS to style the elements
st.markdown("""
    <style>
    /* Adjust the padding of the main block container to move content up */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .title {
        font-family: "Times New Roman", Times, serif;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;  /* Reduced margin */
    }
    .description {
        font-family: "Times New Roman", Times, serif;
        font-size: 20px;
        text-align: center;
        margin: 10px;  /* Reduced margin */
    }
    .section-header {
        font-family: "Times New Roman", Times, serif;
        font-size: 30px;
        text-align: left;
        margin: 20px 0 10px 0;
    }
    .course-link {
        font-family: "Times New Roman", Times, serif;
        font-size: 20px;
        color: #1a73e8; /* Link color */
        cursor: pointer;
    }
    .course-link:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<div class="title">AI Notetaker</div>', unsafe_allow_html=True)

# Updated description
description_text = """
Our AI-powered note-taking application transforms the educational experience by automating the capture of lecture content, benefiting all students, especially those with ADHD, visual or hearing impairments, and mental health challenges. The platform allows students to engage more actively in lectures without the distraction of manual note-taking.
"""

# Description
st.markdown(f'<div class="description">{description_text}</div>', unsafe_allow_html=True)

# Section Header
st.markdown('<div class="section-header">Current Courses</div>', unsafe_allow_html=True)

# Additional sentence and file uploader for syllabus
st.markdown('<div class="description">Please enter the course syllabus to start: 📂</div>', unsafe_allow_html=True)

# Initialize the syllabus in session state
if 'syllabus' not in st.session_state:
    st.session_state['syllabus'] = None

# Syllabus file uploader
syllabus = st.file_uploader("", type=['pdf', 'docx', 'txt'])

# Store the uploaded syllabus in session state
if syllabus is not None:
    st.session_state['syllabus'] = syllabus

# Generate the course link after syllabus upload
if st.session_state['syllabus'] is not None:
    if st.button('Upload File'):
        st.experimental_rerun()

# Check if syllabus is uploaded and show the course link
if st.session_state['syllabus'] is not None:
    st.markdown('<a href="/page1" class="course-link">Introductory Chemistry I: AS.030.101</a>', unsafe_allow_html=True)
