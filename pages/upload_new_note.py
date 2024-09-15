import streamlit as st

# Initialize session state for the files if not already present
if 'audio_file' not in st.session_state:
    st.session_state.audio_file = None
if 'blackboard_file' not in st.session_state:
    st.session_state.blackboard_file = None
if 'personal_file' not in st.session_state:
    st.session_state.personal_file = None
if 'page_generation' not in st.session_state:
    st.session_state.page_generation = False
st.session_state.noteupdateCheck = True
# Set the title for the page
# Display the title and the button on the same line
col1, col2 = st.columns([4, 1])  # Adjust the proportions (4:1) for spacing

with col1:
    st.markdown(f'<div class="title">{st.session_state.currentCourse}</div>', unsafe_allow_html=True)

with col2:
    if st.button('Go back to homepage'):
        st.switch_page('main.py')

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

def save_files():
    import os
    #st.session_state.audio_file
    #st.session_state.blackboard_file
    #st.session_state.personal_file
    blackboard_file = st.session_state.blackboard_file
    course_name = st.session_state.currentCourse
    lecture_name = st.session_state.menu[st.session_state.currentCourse][st.session_state.currentNoteIndex]
    syllabus_file = st.session_state.syllabusList[course_name]
    audio_file = st.session_state.audio_file
    personal_file = st.session_state.personal_file
    os.makedirs("data", exist_ok=True)
    os.makedirs(f"data/{course_name}", exist_ok=True)
    os.makedirs(f"data/{course_name}/{lecture_name}", exist_ok=True)
    os.makedirs(f"data/{course_name}/user_upload", exist_ok=True)
    os.makedirs(f"data/{course_name}/{lecture_name}/user_upload", exist_ok=True)
    with open(os.path.join(os.getcwd(), "data", course_name, "user_upload", "syllabus.pdf"), "wb") as file:
        file.write(syllabus_file.getbuffer())
    with open(os.path.join(os.getcwd(), "data", course_name, lecture_name,"user_upload", blackboard_file.name), "wb") as file: #1 is a placeholder now
        file.write(blackboard_file.getbuffer())
    with open(os.path.join(os.getcwd(), "data", course_name, lecture_name,"user_upload", audio_file.name), "wb") as file: #1 is a placeholder now
        file.write(audio_file.getbuffer())
    with open(os.path.join(os.getcwd(), "data", course_name, lecture_name,"user_upload", personal_file.name), "wb") as file: #1 is a placeholder now
        file.write(personal_file.getbuffer())
# Check if all files are uploaded
if (st.session_state.audio_file is not None and 
    st.session_state.blackboard_file is not None and 
    st.session_state.personal_file is not None):
    # Generate a clickable link with large font size that says "Loading the new AI notebook"
    if st.button('Generate result'):
        save_files() # Save the uploaded files 
        st.session_state.page_generation = True # Change the state to indicate that a new page need to be generated.
        st.switch_page("./pages/note_detail.py")
        st.session_state.page = 'page3'
        st.rerun()  # Reload the app to switch to page 1


