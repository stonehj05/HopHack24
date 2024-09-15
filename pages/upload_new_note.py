import streamlit as st

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
    if st.button('Generate result'):
        st.switch_page("./pages/note_detail.py")
        st.session_state.page = 'page3'
        st.rerun()  # Reload the app to switch to page 1
