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
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Step 1: Load Text Files from a Directory
def load_texts_from_directory(directory):
    texts = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith((".txt",".md")):
                with open(os.path.join(root, filename), 'r', encoding='utf-8') as file:
                    texts.append(file.read())
    return texts

# Step 2: Split Text into Chunks
def split_text_into_chunks(text, chunk_size=100):
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Step 3: Convert Text Chunks to Vectors Using a Pre-trained Model
def convert_chunks_to_vectors(chunks, model):
    return model.encode(chunks)

# Step 4: Build a FAISS Index
def build_faiss_index(vectors):
    d = vectors.shape[1]  # dimension of the vectors
    index = faiss.IndexFlatL2(d)  # L2 distance index
    index.add(np.array(vectors))  # Add vectors to the index
    return index

# Step 5: Perform Similarity Search
def search_similar_chunks(query, model, index, chunked_corpus, k=5):
    query_vector = model.encode([query])  # Convert the query to a vector
    distances, indices = index.search(query_vector, k)  # Search for the top k nearest neighbors
    return [chunked_corpus[i] for i in indices[0]]  # Return the most relevant chunks

# Main function to load data, build the index, and search
def main(directory, query, chunk_size=100, k=5):
    # Load the text files
    texts = load_texts_from_directory(directory)
    
    # Split the texts into chunks
    chunked_corpus = []
    for text in texts:
        chunked_corpus.extend(split_text_into_chunks(text, chunk_size))
    
    # Load a pre-trained model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Convert chunks into vectors
    chunk_vectors = convert_chunks_to_vectors(chunked_corpus, model)
    print(chunk_vectors)
    # Build the FAISS index
    index = build_faiss_index(np.array(chunk_vectors))
    
    # Perform the search
    relevant_chunks = search_similar_chunks(query, model, index, chunked_corpus, k)

    return relevant_chunks



def respond(user_query, context=""):
    # Perform vector search using the query to get relevant context chunks
        # Search the vector database for relevant context
    relevant_contexts = main(f"./data/{st.session_state.currentCourse}", user_query) # Get top 5 most relevant chunks
    print(relevant_contexts)
    context = "\n".join([chunk for chunk in relevant_contexts])  # Combine the chunks
    
    prompt = f"""
        You are a helpful AI assistant helping students to answer their questions on a specfic course. You will read context about the course the student is taking and the recent lecture in the course. The context includes two parts:
        1. The content of course syllabus
        2. The lecture summary for the lecture
        
        Based on this information and your own knowledge, answer students' questions. If you have to generate LaTeX codes for mathematical formulas, make sure they can get compiled. Include an answer and detailed explanations for students' questions. Make sure your answer is not in Do not include any extra content.
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
            st.write(text[0])
            return text[0]
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
        response,ctx = respond(speech_text)
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
    response,ctx = respond(user_input)
    st.session_state.chat_history.append(f"Bot: {response} \nContext: {ctx}")