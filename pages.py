import streamlit as st
# Define the content for Page 1
def page1():
    # Set page configuration
    st.write(page_title="Course Notebook", layout="wide")

    # Ensure there is a valid course index
    if len(st.session_state.courseIndex) == 0:
        st.error("No course selected.")
        return
    else:
        st.write("good")
        return

    # Get the most recent course that was selected
    current_index = courseIndex[-1]  # Get the latest course index
    course_name = courseList[current_index] if len(courseList) > current_index else "Course Name"
    syllabus = syllabusList.get(current_index, "No syllabus available")

    # Display the course name
    st.markdown(f"<h2 style='text-align: center; margin-top: 0;'>{course_name}</h2>", unsafe_allow_html=True)

    # Display the course summary or syllabus (for now, a static summary can be used)
    summary = "This course introduces students to the fundamentals of chemistry, including atomic structure, periodic trends, and chemical reactions."
    st.markdown('<div class="text-content">' + summary + '</div>', unsafe_allow_html=True)

    # Example: number of pictures we have (range 0-6)
    count = 0  # Default count of images
    images = ["Notebook.png"] * count  # List of image paths
    links = [f"Notebook {i+1}" for i in range(count)]  # Corresponding links

    if count != 0:
        # Create a dynamic layout for images and links, with all elements left-aligned
        columns = st.columns(count)
        for i, col in enumerate(columns):
            with col:
                if i < count:
                    st.image(images[i], width=150)  # Adjust the image size
                    st.markdown(f'<a href="/page2" target="_self">{links[i]}</a>', unsafe_allow_html=True)

        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # Create a new notebook text input with a large font
    st.markdown('<p class="input-title">Create a new notebook by entering its name:</p>', unsafe_allow_html=True)
    new_notebook_name = st.text_input("", value="", placeholder="Enter Notebook Name Here")

    # Handle the creation of a new notebook
    if new_notebook_name:
        st.markdown(f"Notebook '{new_notebook_name}' created!")
        st.markdown('<a href="/page2" target="_self" class="upload-link">Upload further information</a>', unsafe_allow_html=True)

    # Adjust the layout to use only the upper part of the page
    st.markdown(
        """
        <style>
        .css-18e3th9 {
            padding-top: 2rem;  /* Reduce the top padding */
        }
        .css-1d391kg { 
            padding-top: 2rem;  /* Reduce padding for narrow pages */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button('Go back to homepage'):
        st.session_state.page = 'main'
        st.rerun()  # Reload the app to switch to the main page


def page2():
    # Initialize session state for the files if not already present
    if 'audio_file' not in st.session_state:
        st.session_state.audio_file = None
    if 'blackboard_file' not in st.session_state:
        st.session_state.blackboard_file = None
    if 'personal_file' not in st.session_state:
        st.session_state.personal_file = None

    # Set the title for the page
    st.title("Upload further information")

    # Add file upload options with instructions (styled to be large)
    st.markdown("<h2>Please upload class audio:</h2>", unsafe_allow_html=True)
    st.session_state.audio_file = st.file_uploader("Upload class audio:", type=["mp3", "wav", "m4a"])

    st.markdown("<h2>Please upload blackboard writing (including zip files):</h2>", unsafe_allow_html=True)
    st.session_state.blackboard_file = st.file_uploader("Upload blackboard writing:", type=["jpg", "jpeg", "png", "pdf", "zip"])

    st.markdown("<h2>Please upload your own file:</h2>", unsafe_allow_html=True)
    st.session_state.personal_file = st.file_uploader("Upload your own file:", type=["pdf", "docx", "txt"])

    # Optional: Display the filenames once uploaded
    if st.session_state.audio_file:
        st.write(f"Uploaded audio file: {st.session_state.audio_file.name}")

    if st.session_state.blackboard_file:
        st.write(f"Uploaded blackboard file: {st.session_state.blackboard_file.name}")

    if st.session_state.personal_file:
        st.write(f"Uploaded personal file: {st.session_state.personal_file.name}")

    # Check if all files are uploaded
    if (st.session_state.audio_file is not None and 
        st.session_state.blackboard_file is not None and 
        st.session_state.personal_file is not None):
        
        # Generate a clickable link with large font size that says "Loading the new AI notebook"
        page_link = f"<a href='/page3' style='font-size:36px;'>Loading the new AI notebook</a>"
        st.markdown(page_link, unsafe_allow_html=True)


def page3():
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
    st.markdown('<a href="/page1" class="return-button">Return to Page 1</a>', unsafe_allow_html=True)

    # Example content in the notebook page
    st.write("This is the content of your notebook.")

def page4():
    # Set page configuration
    st.set_page_config(page_title="Course Notebook", layout="wide")

    # Initialize session state for the notebook name
    if 'notebookName' not in st.session_state:
        st.session_state['notebookName'] = None  # Default value if not set

    # Retrieve the syllabus from session_state (optional, if needed)
    syllabus = st.session_state.get('syllabus', None)
    summary = "This course introduces students to the fundamentals of chemistry, including atomic structure, periodic trends, and chemical reactions."

    # Apply CSS to add margin and increase font size for the summary and text input
    st.markdown(
        """
        <style>
        .text-content {
            margin-left: 20px;  /* Push text two spaces (adjustable) */
            font-size: 1.2rem;  /* Increase font size for summary */
            margin-bottom: 30px;  /* Add margin below the summary */
        }
        .input-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .spacer {
            margin-top: 40px;  /* Add space above the notebook input */
        }
        .upload-link {
            font-size: 2rem;  /* Make the "Upload further information" text as large as the title */
            text-align: center;
            display: block;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the course title at the top
    st.markdown("<h2 style='text-align: center; margin-top: 0;'>Introductory Chemistry I: AS.030.101</h2>", unsafe_allow_html=True)

    # Display the course summary
    st.markdown('<div class="text-content">' + summary + '</div>', unsafe_allow_html=True)

    # Create a two-column layout for the images and links, aligned horizontally to the left
    col_left, col_mid, col_right = st.columns([1 ,1, 6])  # Adjust the column proportions (1:6) for left alignment

    with col_left:
        # First image and link
        st.image("Notebook.png", width=150)  # Make the image small
        st.markdown("""
        <div style="display: flex; justify-content: space-between;">
            <span style="text-align: left;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/page2" target="_self">Notebook 1</a></span>
        </div>
        """, unsafe_allow_html=True)

    with col_mid:
        # Second image and link
        st.image("Notebook.png", width=150)  # Make the image small
        st.markdown("""
        <div style="display: flex; justify-content: space-between;">
            <span style="text-align: left;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/page2" target="_self">Notebook 2</a></span>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        # Second image and link
        st.image("Notebook.png", width=150)  # Make the image small
        st.markdown("""
        <div style="display: flex; justify-content: space-between;">
            <span style="text-align: left;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/page2" target="_self">Notebook 3</a></span>
        </div>
        """, unsafe_allow_html=True)

    # Add a blank space before the text input field
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # Create a new notebook text input with a large font
    st.markdown('<p class="input-title">Create a new notebook by entering its name:</p>', unsafe_allow_html=True)
    notebook_name = st.text_input("", value="", placeholder="Enter notebook name here")

    # If a notebook name is entered, store it in session state and display the link
    if notebook_name:
        st.session_state['notebookName'] = notebook_name
        st.markdown(f"Notebook '{st.session_state['notebookName']}' created!")

        # Display the link to page2 for further information with large font size
        st.markdown('<a href="/page2" target="_self" class="upload-link">Upload further information</a>', unsafe_allow_html=True)

    # Adjust the layout to use only the upper part of the page
    st.markdown(
        """
        <style>
        .css-18e3th9 {
            padding-top: 2rem;  /* Reduce the top padding */
        }
        .css-1d391kg { 
            padding-top: 2rem;  /* Reduce padding for narrow pages */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def page5():
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
    st.markdown('<div class="description">Please enter the new course syllabus to start: 📂</div>', unsafe_allow_html=True)

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