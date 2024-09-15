import streamlit as st
import sys
sys.path.insert(0, "..")
from image2text.utils import *
api_key = get_openai_api_key()
from voice2text.voice_text import transcribe_audio_files
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

import os
from dsp import VectorDB, FileLoader, SimpleEncoder

def build_vector_db(data_folder):
    # Create a VectorDB instance (simple vector storage)
    vector_db = VectorDB(encoder=SimpleEncoder())  # SimpleEncoder can be customized for better results
    
    #  Recursively Load all text files from the given data folder
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            if file.endswith(".txt",".md"):
                file_path = os.path.join(data_folder, file_name)
                loader = FileLoader(file_path)
                
                # Add each document to the vector database
                for chunk in loader.load_chunks():
                vector_db.add(chunk['text'], chunk['meta'])  # Store text and metadata (if any)
           
    
    return vector_db



def respond(user_query, context="", vector_db=None):
    # Perform vector search using the query to get relevant context chunks
    if vector_db is not None:
        # Search the vector database for relevant context
        relevant_contexts = vector_db.search(user_query, top_k=5)  # Get top 5 most relevant chunks
        context = "\n".join([chunk['text'] for chunk in relevant_contexts])  # Combine the chunks
    
    prompt = f"""
        You are a helpful AI assistant helping students to answer their questions on a specfic course. You will read context about the course the student is taking and the recent lecture in the course. The context includes two parts:
        1. The content of course syllabus
        2. The lecture summary for the lecture
        
        Based on this information and your own knowledge, answer students' questions. If you have to generate LaTeX codes for mathematical formulas, make sure they can get compiled. Include an answer and detailed explanations for students' questions. Do not include any extra content.
        Question: {user_query}
        Context: {context}
    """
    
    messages = prepare_messages(prompt)
    response = gpt_api_call(messages, 0.0, api_key)
    
    return response, context


# Function to recognize speech input
def recognize_speech_from_mic():
    with sr.Microphone() as source:
        st.info("Adjusting microphone for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source)
        st.info("Listening...")
        audio = r.listen(source)

        wav_output = 'test.wav'
        with open(wav_output, 'wb') as f:
            f.write(audio.get_wav_data())

        try:
            # Use Google Web Speech API to recognize speech
            text = transcribe_audio_files(["test.wav"])
            st.write(text)
            return text
        except sr.RequestError:
            return "API unavailable"
        except sr.UnknownValueError:
            return "Unable to recognize speech"

# Load the vector database
course_name = st.session_state.currentCourse
data_folder = f"./data/{course_name}"
vector_db = build_vector_db(data_folder)


# Streamlit UI
st.title("Speech-to-Text Chatbox")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input from user via button
if st.button("Click and Speak"):
    speech_text = recognize_speech_from_mic()
    
    # Append recognized speech to chat history
    if speech_text:
        st.session_state.chat_history.append(f"You: {speech_text}")
        # Generate response based on speech input
        response,ctx = respond(speech_text,vector_db=vector_db)
        st.session_state.chat_history.append(f"Bot: {response} \nContext: {ctx}")
        
# Display chat history
st.subheader("Chat History")
for chat in st.session_state.chat_history:
    st.write(chat)

# Text input box for typed text
user_input = st.text_input("Type your message:")

if user_input:
    st.session_state.chat_history.append(f"You: {user_input}")
    # Generate response based on typed input
    response,ctx = respond(user_input,vector_db=vector_db)
    st.session_state.chat_history.append(f"Bot: {response} \nContext: {ctx}")