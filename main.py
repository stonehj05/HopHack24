import streamlit as st
from pages import *

#A dictionary that correspond the courseIndex to the number notebooks it has right now {int : int}
if 'courseNoteBookNumberCount' not in st.session_state:
     st.session_state.courseNoteBookNumberCount = {}

#A int that keep track the current index of course, which correspond to the order that they are added
if 'courseIndex' not in st.session_state:
    st.session_state.courseIndex = 0

#A dictionary that link index to courseName {int : string}
if 'courseDictionary' not in st.session_state:
    st.session_state.courseDictionary = {}

#A dictionary that link course name to its syllabus {string : file}
if 'syllabusList' not in st.session_state:
    st.session_state.syllabusList = {}


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
        margin: 5px 0 10px 0;
    }
    .course-link {
        font-size: 30px;
        font-weight: bold;
        color: #3498db;
        text-decoration: none;
    }
    .larger-text {
        font-size: 30px;
        font-weight: bold;
    }
    .input-label {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# # Initialize session state to keep track of pages
# if 'page' not in st.session_state:
#     st.session_state.page = 'main'

# Define the main page content (this will be the default landing page)
def main_page():
    syllabus = None
    Course_name = None
    st.markdown('<div class="title">AI Notetaker</div>', unsafe_allow_html=True)

    description_text = """
    Our AI-powered note-taking application transforms the educational experience by automating the capture of lecture content, benefiting all students, especially those with ADHD, visual or hearing impairments, and mental health challenges. The platform allows students to engage more actively in lectures without the distraction of manual note-taking.
    """
    st.markdown(f'<div class="description">{description_text}</div>', unsafe_allow_html=True)
    if (st.session_state.courseIndex == 0):
        st.markdown('<div class="larger-text">Please enter the new course syllabus to start: 📂</div>', unsafe_allow_html=True)
    else:
        num_images = st.session_state.courseIndex

        # Display images in a left-aligned format
        cols = st.columns(10)  # Creates 10 columns for better left alignment
        st.write(num_images)
        for i in range(num_images):
            with cols[0]:  # Use the first column (leftmost)
                st.image('Folder.png', use_column_width=True)
                if st.button(f"Go to Note Page {i+1}", key=f"button_{i}"):
                    st.session_state.page = f"notepage{i+1}"

    # Text input for notebook name with larger label
    st.markdown('<div class="input-label">Enter Course Name</div>', unsafe_allow_html=True)
    Course_name = st.text_input("", value="", placeholder="Enter Course name here")
    if Course_name:
        if Course_name not in st.session_state.courseDictionary.values(): 
            st.session_state.courseIndex += 1
            st.session_state.courseDictionary[st.session_state.courseIndex] = Course_name
        st.write("Course Name Entered Successfully")
    # Syllabus file uploader
    syllabus = st.file_uploader("", type=['pdf', 'docx', 'txt'])

    if syllabus is not None:
        st.session_state.syllabusList[Course_name] = syllabus
    # Conditionally display the button to go to Page 1 only if both the syllabus is uploaded and the notebook name is entered
    if syllabus is not None and Course_name is not None:
        st.markdown('<div class="description">Syllabus uploaded and notebook name provided!</div>', unsafe_allow_html=True)
        st.write('page' + str(st.session_state.courseIndex))
        # Show button to navigate to Page 1 only after inputs are given
        if st.button('Go to ' + Course_name):
            st.session_state.page = 'page' + str(st.session_state.courseIndex) # TODO: Need to change to storing session state.course_name
            st.rerun()  # Reload the app to switch to page 1

# Dynamically show content based on the current page
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'page1':
   st.switch_page("course_page.py") 
elif st.session_state.page == 'page2':
   st.switch_page("upload_new_note.py") 
elif st.session_state.page == 'page3':
   st.switch_page("note_detail.py") 