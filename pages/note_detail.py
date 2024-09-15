import streamlit as st
import os

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
st.page_link("./pages/course_page.py", label="Return to Course Page", icon="🏠")
# st.markdown('<a href="/page1" class="return-button">Return to Page 1</a>', unsafe_allow_html=True)

# Example content in the notebook page
st.write("This is the content of your notebook.")
