import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1
#st.session_state.audio_file
#st.session_state.blackboard_file
#st.session_state.personal_file
blackboard_file = st.session_state.blackboard_file
course_name = st.session_state.courseDictionary[1]
syllabus_file = st.session_state.syllabusList[course_name]
audio_file = st.session_state.audio_file
personal_file = st.session_state.personal_file
os.makedirs("data", exist_ok=True)
os.makedirs(f"data/{course_name}", exist_ok=True)
os.makedirs(f"data/{course_name}/1", exist_ok=True)
with open(os.path.join(os.getcwd(), "data", course_name, syllabus_file.name), "wb") as file:
    file.write(syllabus_file.getbuffer())
with open(os.path.join(os.getcwd(), "data", course_name, "1", blackboard_file.name), "wb") as file: #1 is a placeholder now
    file.write(blackboard_file.getbuffer())
with open(os.path.join(os.getcwd(), "data", course_name, "1", audio_file.name), "wb") as file: #1 is a placeholder now
    file.write(audio_file.getbuffer())
with open(os.path.join(os.getcwd(), "data", course_name, "1", personal_file.name), "wb") as file: #1 is a placeholder now
    file.write(personal_file.getbuffer()))

'...and now we\'re done!'
