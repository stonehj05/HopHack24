import streamlit as st

def course_image_display(fileName, n):
    cols = st.columns(n)  # Create one column per image
    # Iterate over images and display each one with its corresponding button
    for i, col in enumerate(cols):
        with col:
            st.image(fileName, width=100)
            if st.button(st.session_state.courseDictionary[i+1], key=f"button_{i}" + str(st.session_state.courseIndex)):
                st.session_state.currentCourse  = st.session_state.courseDictionary[i+1]
                # st.session_state.courseIndex = list(st.session_state.courseDictionary.keys.index)[list(st.session_state.courseDictionary.values).index((st.session_state.currentCourse))]
                st.switch_page("pages/course_page.py")

def note_image_display(fileName, n):
    # Ensure noteDictionary is available in session state
    if 'noteDictionary' not in st.session_state:
        st.error("noteDictionary not found in session state.")
        return

    note_dict = st.session_state.noteDictionary

    # Create columns for each image
    cols = st.columns(n)
    
    # Iterate over images and display each one with its corresponding button
    for i, col in enumerate(cols):
        with col:
            st.image(fileName, width=100)

            # Get the note name using the index i+1
            note_name = note_dict.get(i + 1, None)

            if note_name:
                if st.button(note_name):
                    st.session_state.currentNote = note_name
                    #st.switch_page('./pages/upload_new_note.py')

            else:
                st.error(f"Note index {i} is missing in noteDictionary.")

# if __name__ == '__main__':
#     image_display("folder.PNG",6)
