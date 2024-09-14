import streamlit as st

from pages import page1

courseNoteBookNumberCount = {"first": 0, "second": 0, "third": 0, "forth": 0, "fifth": 0}
courseList = []
courseIndex = []
courseDictionary = {}
syllabusList = {}
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

# Initialize session state to keep track of pages
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Define the main page content (this will be the default landing page)
def main_page(courseList, courseIndex, courseDictionary, syllabusList):
    syllabus = None
    Course_name = None
    st.markdown('<div class="title">AI Notetaker</div>', unsafe_allow_html=True)

    description_text = """
    Our AI-powered note-taking application transforms the educational experience by automating the capture of lecture content, benefiting all students, especially those with ADHD, visual or hearing impairments, and mental health challenges. The platform allows students to engage more actively in lectures without the distraction of manual note-taking.
    """
    st.markdown(f'<div class="description">{description_text}</div>', unsafe_allow_html=True)
    if (len(courseList) == 0):
        st.markdown('<div class="larger-text">Please enter the new course syllabus to start: 📂</div>', unsafe_allow_html=True)
    else:
        pictureNumber = len(courseList)


    # Text input for notebook name with larger label
    st.markdown('<div class="input-label">Enter Course Name</div>', unsafe_allow_html=True)
    Course_name = st.text_input("", value="", placeholder="Enter Course name here")
    if Course_name:
        courseIndex.append(1)
        courseDictionary[Course_name] = len(courseIndex)
        st.write("Course Name Entered Successfully")
    # Syllabus file uploader
    syllabus = st.file_uploader("", type=['pdf', 'docx', 'txt'])

    if syllabus is not None:
        syllabusList[len(courseIndex)] = syllabus
    # Conditionally display the button to go to Page 1 only if both the syllabus is uploaded and the notebook name is entered
    if syllabus is not None and Course_name is not None:
        st.markdown('<div class="description">Syllabus uploaded and notebook name provided!</div>', unsafe_allow_html=True)

        # Show button to navigate to Page 1 only after inputs are given
        if st.button('Go to ' + Course_name):
            st.session_state.page = 'page' + str(len(courseIndex))
            st.rerun()  # Reload the app to switch to page 1

# Dynamically show content based on the current page
if st.session_state.page == 'main':
    main_page(courseList, courseIndex, courseDictionary, syllabusList)
elif st.session_state.page == 'page1':
    page1()
