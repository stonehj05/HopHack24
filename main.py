import streamlit as st
from pages import *
from picture import *
from previousNoteReader import *
from pathlib import Path

if 'noteupdateCheck' not in st.session_state:
    st.session_state.noteupdateCheck = True

#A dictionary that correspond the courseIndex to the number notebooks it has right now {int : int}
if 'courseNoteBookNumberCount' not in st.session_state:
    st.session_state.courseNoteBookNumberCount = {}

#A dictionary that correspond the courseIndex to the number notebooks it has right now {int : int}
# if 'currentIndex' not in st.session_state:
#     st.session_state.currentIndex = {}

#A dictionary that correspond the courseName to inner dictionary from noteindex to notename {string : {int : string}}
if 'menu' not in st.session_state:
    st.session_state.menu = {}

if 'currentNoteIndex' not in st.session_state:
    st.session_state.currentNoteIndex = 1

#A int that keep track the current index of course, which correspond to the order that they are added
if 'courseIndex' not in st.session_state:
    st.session_state.courseIndex = 0

#A dictionary that link index to courseName {int : string}
if 'courseDictionary' not in st.session_state:
    st.session_state.courseDictionary = {}

#A dictionary that link course name to its syllabus {string : file}
if 'syllabusList' not in st.session_state:
    st.session_state.syllabusList = {}

if 'currentCourse' not in st.session_state:
    st.session_state.currentCourse = ""


# Set page config
st.set_page_config(page_title="AI Notetaker", page_icon="📝", layout="wide")
#previousNoteReader()
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
syllabus = None
Course_name = None
st.markdown('<div class="title">AI Notetaker</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 4, 1])  # Adjust the proportions (4:1) for spacing

with col2:
    description_text = """
    Our AI-powered note-taking application transforms the educational experience by automating the capture of lecture content, benefiting all students, especially those with ADHD, visual or hearing impairments, and mental health challenges. The platform allows students to engage more actively in lectures without the distraction of manual note-taking.
    """
    st.markdown(f'<div class="description">{description_text}</div>', unsafe_allow_html=True)

# if (st.session_state.courseIndex == 0):
#     st.markdown('<div class="larger-text">Please enter the new course syllabus to start: 📂</div>', unsafe_allow_html=True)
# else:
#     course_image_display("folder.PNG", st.session_state.courseIndex)

# First read courses from previous paths and initialize automatically if not already done
data_folder_path = Path('data')

if not st.session_state.courseDictionary:
    if data_folder_path.exists():
        # Get the subfolders with their paths
        subfolders_with_paths = [(f.name, f) for f in data_folder_path.iterdir() if f.is_dir()]
        
        if subfolders_with_paths:
            for subfolder, subpath in subfolders_with_paths:
                Course_name = str(subfolder)
                if Course_name not in st.session_state.courseDictionary.values():
                    notebookFolder = [(fn.name, fn) for fn in subpath.iterdir() if fn.is_dir()]
                    st.session_state.courseIndex += 1
                    st.session_state.courseDictionary[st.session_state.courseIndex] = Course_name
                    st.session_state.menu[Course_name] = {}
                    noteIndex = 1
                    for subnotepage, subnotepath in notebookFolder:
                        notepage = str(subnotepage)
                        if notepage not in st.session_state.menu[Course_name].values():
                            st.session_state.menu[Course_name][noteIndex] = notepage
                            noteIndex += 1
                            
                if not st.session_state.currentCourse:
                    st.session_state.currentCourse = Course_name
            st.write(f"Automatically loaded courses: {', '.join(st.session_state.courseDictionary.values())}")
            
            # Display the folder image and the first course if available
            course_image_display("folder.PNG", st.session_state.courseIndex)
        else:
            st.markdown('<div class="larger-text">No existing courses found. Please enter a new course syllabus to start: 📂</div>', unsafe_allow_html=True)
    else:
        st.error(f"The specified folder '{data_folder_path}' does not exist. Please create it and add courses.")
else:
    # If courses are already loaded in the session, display the current course
    st.write(f"Current course: {st.session_state.currentCourse}")
    course_image_display("folder.PNG", st.session_state.courseIndex)

# Text input for notebook name with larger label
st.markdown('<div class="input-label">Enter Course Name</div>', unsafe_allow_html=True)
Course_name = st.text_input("", value="", placeholder="Enter Course name here")
if Course_name:
    if Course_name not in st.session_state.courseDictionary.values(): 
        st.session_state.courseIndex += 1
        # st.session_state.currentIndex = st.session_state.courseIndex
        st.session_state.courseDictionary[st.session_state.courseIndex] = Course_name
        st.session_state.currentCourse = Course_name
        st.write("Course Name Entered Successfully")
        #course_image_display("folder.PNG", st.session_state.courseIndex)
# Syllabus file uploader
syllabus = st.file_uploader("", type=['pdf', 'docx', 'txt'])

if syllabus is not None:
    st.session_state.syllabusList[Course_name] = syllabus
# Conditionally display the button to go to Page 1 only if both the syllabus is uploaded and the notebook name is entered
if syllabus is not None and Course_name is not None:
    st.markdown('<div class="description">Syllabus uploaded and notebook name provided!</div>', unsafe_allow_html=True)
    # Show button to navigate to Page 1 only after inputs are given
    if st.button('Go to ' + Course_name):
        st.session_state.noteupdateCheck = True
        st.switch_page("pages/course_page.py")