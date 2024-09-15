import streamlit as st

def course_image_display(fileName, n):
    cols = st.columns(n)  # Create one column per image
    # Iterate over images and display each one with its corresponding button
    for i, col in enumerate(cols):
        with col:
            st.image(fileName, width=150)
            if st.button("  " + st.session_state.courseDictionary[i+1], key=f"button_{i}" + str(st.session_state.courseIndex)):
                st.session_state.currentCourse  = st.session_state.courseDictionary[i+1]
                st.switch_page("pages/course_page.py")

def note_image_display(fileName, n, noteDictionary):
    # Create columns for each image
    cols = st.columns(n)
    
    # Iterate over images and display each one with its corresponding button
    for i, col in enumerate(cols):
        with col:
            st.image(fileName, width=100)

            # Get the note name using the index i+1
            note_name = noteDictionary.get(i + 1, None)

            if note_name:
                if st.button(note_name):
                    st.session_state.currentNote = st.session_state.menu[st.session_state.currentCourse][i + 1]
                    st.switch_page("pages/course_page.py")

            else:
                st.error(f"Note index {i + 1} is missing in noteDictionary.")

# if __name__ == '__main__':
#     image_display("folder.PNG",6)
