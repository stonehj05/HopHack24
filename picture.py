import streamlit as st

def image_display(fileName, n):
    cols = st.columns(n)  # Create one column per image
    # Iterate over images and display each one with its corresponding button
    for i, col in enumerate(cols):
        with col:
            st.image(fileName, width=100)
            if st.button(st.session_state.courseDictionary[i+1], key=f"button_{i}" + str(st.session_state.courseIndex)):
                st.session_state.currentCourse  = st.session_state.courseDictionary[i+1]
                st.switch_page("pages/course_page.py")

# if __name__ == '__main__':
#     image_display("folder.PNG",6)
