import streamlit as st
import os
from file_handle import *
import json
from generate_note import generate_note

### LOAD DATA ###
course_name = st.session_state.currentCourse
note_name = st.session_state.menu[st.session_state.currentCourse][st.session_state.currentNoteIndex]

note_path = f"../data/{course_name}/{note_name}"
if not os.path.exists(os.path.join(note_path, "note.md")):
    syllabus_file = st.session_state.syllabusList[course_name]
    audio_file = st.session_state.audio_file
    personal_file = st.session_state.personal_file
    blackboard_file = st.session_state.blackboard_file
    syllabus_content = read_syllabus(syllabus_file.name, course_name)
    blackboard_images = read_blackboard(blackboard_file.name, course_name, note_name)
    handnote_images = read_handnote(personal_file.name, course_name, note_name)
    audio_file_path = os.path.join(os.getcwd(), "data", course_name, note_name, "user_upload", audio_file.name)
    generate_note(blackboard_images, [audio_file_path], handnote_images, context=syllabus_content, course_name=course_name, lecture_name=note_name)
with open(f"./data/{course_name}/{note_name}/questions.json", "r") as file:
    questions = json.load(file)
with open(f"./data/{course_name}/{note_name}/note.md", "r") as file:
    note = file.read()
with open(f"./data/{course_name}/{note_name}/graph_data_with_topic.json", "r") as file:
    graph_data = json.load(file)

st.session_state.note_text_raw=note

st.session_state.question_list=questions

def blur_match(topic,section,subsection):
    # topic_parts = topic.split("@")
    # if len(topic_parts) == 2:
    #     topic_section, topic_subsection = topic_parts
    #     return topic_section == section and topic_subsection == subsection
    # return False
    # Create a blurred matching function, allowing for partial matches between section and subsection to topic where all special characters are ignored
    topic = topic.replace("_", " ").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
    section = section.replace("_", " ").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
    subsection = subsection.replace("_", " ").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
    return section.lower() in topic.lower() and subsection.lower() in topic.lower()


# Set page configuration
st.set_page_config(page_title="Notebook Page", layout="wide")


st.session_state.note_partition_dict = note2dict(st.session_state.note_text_raw, course_name, note_name)

# Title stored in session state
if 'lecture_name' not in st.session_state:
    st.session_state.lecture_name = "POWER NOTES"
st.title(st.session_state.lecture_name)


# Add a checkbox trigger at the top right corner
show_questions = st.checkbox("Show AI-Gen Questions", value=False)

# Iterate through sections and subsections in the note_partition_dict
for section, subsections in st.session_state.note_partition_dict.items():
    st.header(section)
    # print("section",section)
    # print("subsections",subsections)
    for subsection, content in subsections.items():
        st.subheader(subsection)
        
        # Create a container for each subsection with columns inside
        with st.container():
            if show_questions:
                # When questions are shown, use a 2-column layout
                col1, col2 = st.columns([2, 1])
            else:
                # When questions are hidden, use only one column
                col1 = st.container()
            # LEFT COLUMN: Display the subsection content (text)
            with col1:
                st.markdown(content)
                # check if the subsection has any graphs
                related_graphs = [
                    graph for graph in graph_data['Diagrams'] if blur_match(graph['topic'], f"{section}", f"{subsection}")
                ]
                if related_graphs:
                    for graph in related_graphs:
                        st.write(f"**Graph**: {graph['Summary']}")
                        st.image(f"./data/{course_name}/{note_name}/image{graph['Index']}.png")
            
            # RIGHT COLUMN: Display related questions (if any) from question_list
            if not show_questions:
                continue
            with col2:
                print("st.session_state.question_list",st.session_state.question_list)
                related_questions = [
                    q for q in st.session_state.question_list['questions']
                    if blur_match(q['topic'], f"{section}",f"{subsection}")
                ]
                # print("related_questions",related_questions)
                if related_questions:
                    for question_data in related_questions:
                        # st.write(f"Questions for **{section} : {subsection}**")
                        # Create tabs for different question difficulty levels
                        tab1, tab2, tab3 = st.tabs(["Conceptual", "Moderate", "Challenging"])
                        
                        # Conceptual questions
                        with tab1:
                            for question in question_data['levels']:
                                if question['tag'] == "Conceptual":
                                    st.markdown(f"### **Question**: {question['question']}")
                                    # st.text_input("Your answer:", key=f"{section}_{subsection}_conceptual")
                                    if 'hint' in question:
                                        with st.expander("💡Hint (Click to expand)"):
                                            st.write(question['hint'])
                                    with st.expander("📝Answer (Click to expand)"):
                                        st.write(question['answer'])
                        
                        # Easy questions
                        with tab2:
                            for question in question_data['levels']:
                                if question['tag'] == "Easy":
                                    st.markdown(f"### **Question**: {question['question']}")
                                    # st.text_input("Your answer:", key=f"{section}_{subsection}_easy")
                                    if 'hint' in question:
                                        with st.expander("💡Hint (Click to expand)"):
                                            st.write(question['hint'])
                                    with st.expander("📝Answer (Click to expand)"):
                                        st.write(question['answer'])
                        
                        # Challenging questions
                        with tab3:
                            for question in question_data['levels']:
                                if question['tag'] == "Challenging":
                                    st.markdown(f"### **Question**: {question['question']}")
                                    # st.text_input("Your answer:", key=f"{section}_{subsection}_challenging")
                                    if 'hint' in question:
                                        with st.expander("💡Hint (Click to expand)"):
                                            st.write(question['hint'])

                                    with st.expander("📝Answer (Click to expand)"):
                                        st.write(question['answer'])
                else:
                    st.write("No questions available for this section.")

# Footer with progress metric
st.markdown("---")
st.metric(label="Progress", value="50%", delta="5%")

# Add a button to stop execution
if st.button("Stop the process"):
    st.stop()

st.success('Page Loaded Successfully!')