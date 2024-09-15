import streamlit as st

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
    .text-content {
        margin-left: 20px;  /* Push text two spaces */
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

# Ensure there is a valid course index
if st.session_state.courseIndex == 0:
    st.error("No course selected.")

# Get the most recent course index and course name
course_name = st.session_state.courseDictionary[1]  # Get the course name based on the index
syllabus = st.session_state.syllabusList.get(1, "No syllabus available")

# Display the course title at the top
st.markdown(f"<h2 style='text-align: center; margin-top: 0;'>{course_name}</h2>", unsafe_allow_html=True)

# Display the course summary or syllabus
summary = "This course introduces students to the fundamentals of chemistry, including atomic structure, periodic trends, and chemical reactions."
st.markdown('<div class="text-content">' + summary + '</div>', unsafe_allow_html=True)

# Create a two-column layout for the images and links, aligned horizontally to the left
col_left, col_mid, col_right = st.columns([1, 1, 6])  # Adjust the column proportions (1:6) for left alignment

with col_left:
    # First image and link
    st.image("Notebook.png", width=150)  # Make the image small
    st.page_link("upload_new_note.py", label="Notebook 1", icon="🏠")
    # st.markdown("""
    # <div style="display: flex; justify-content: space-between;">
    #     <span style="text-align: left;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/page2" target="_self">Notebook 1</a></span>
    # </div>
    # """, unsafe_allow_html=True)

with col_mid:
    # Second image and link
    st.image("Notebook.png", width=150)  # Make the image small
    st.page_link("upload_new_note.py", label="Notebook 2", icon="🏠")
    # st.markdown("""
    # <div style="display: flex; justify-content: space-between;">
    #     <span style="text-align: left;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/page2" target="_self">Notebook 2</a></span>
    # </div>
    # """, unsafe_allow_html=True)

with col_right:
    # Third image and link
    st.image("Notebook.png", width=150)  # Make the image small
    st.page_link("upload_new_note.py", label="Notebook 3", icon="🏠")
    # st.markdown("""
    # <div style="display: flex; justify-content: space-between;">
    #     <span style="text-align: left;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/page2" target="_self">Notebook 3</a></span>
    # </div>
    # """, unsafe_allow_html=True)

# Add a blank space before the text input field
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Create a new notebook text input with a large font (integrating page4 functionality)
st.markdown('<p class="input-title">Create a new notebook by entering its name:</p>', unsafe_allow_html=True)
new_notebook_name = st.text_input("", value="", placeholder="Enter Notebook Name Here")

# Handle the creation of a new notebook
if st.button('Generate result'):
        st.switch_page('./pages/upload_new_note.py')
        # st.session_state.page = 'page2'
        # st.rerun()  # Reload the app to switch to page 1

# Button to return to the homepage
if st.button('Go back to homepage'):
    st.switch_page('main.py')
    # st.session_state.page = 'main'
    # st.rerun()  # Reload the app to switch to the main page