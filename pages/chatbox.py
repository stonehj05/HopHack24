import streamlit as st
import sys
sys.path.insert(0, "..")
from voice2text.voice_text import transcribe_audio_files
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

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
        
# Display chat history
st.subheader("Chat History")
for chat in st.session_state.chat_history:
    st.write(chat)

# Text input box for typed text
user_input = st.text_input("Type your message:")

if user_input:
    st.session_state.chat_history.append(f"You: {user_input}")