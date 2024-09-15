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

# Placeholder function to respond to user questions
def respond(question, context=""):
    prompt = f"""
        You are a helpful AI assistant helping students to answer there questions. You will read context about the course the student is taking and the recent lecture in the course. The context include two parts
        1. The content of course syllabus
        2. The lecture summary for the lecture
        Based on these information and your own knowledge, answer students' questions. If you have to generate latex codes for mathematical formulas, make sure they can get compiled. Include answer and detailed explanations for students' questions. Do not include any extra contents.
        Question: {question}
        Context: {context}
    """
    messages = prepare_messages(prompt)
    response = gpt_api_call(messages, 0.0, api_key)
    return response

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
        response = respond(speech_text)
        st.session_state.chat_history.append(f"Bot: {response}")
        
# Display chat history
st.subheader("Chat History")
for chat in st.session_state.chat_history:
    st.write(chat)

# Text input box for typed text
user_input = st.text_input("Type your message:")

if user_input:
    st.session_state.chat_history.append(f"You: {user_input}")
    # Generate response based on typed input
    response = respond(user_input)
    st.session_state.chat_history.append(f"Bot: {response}")