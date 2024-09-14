import streamlit as st

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
