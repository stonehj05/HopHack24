# import speech_recognition as sr
# from datetime import datetime
# import numpy as np
# from scipy.io import wavfile
# from moviepy.editor import AudioFileClip  # Import moviepy for conversion
# import os
# import time

# # MP3 to WAV conversion using moviepy
# mp3_file_path = r'/home/yru2/HopHack24/voice2text/Health Recovery Voiceover.mp3'
# wav_output_path = r'/home/yru2/HopHack24/voice2text/WAV_AUDIO_FILE.wav'

# def convert_mp3_to_wav(mp3_path, wav_path):
#     audio_clip = AudioFileClip(mp3_path)
#     audio_clip.write_audiofile(wav_path, codec='pcm_s16le')  # Save as WAV file

# convert_mp3_to_wav(mp3_file_path, wav_output_path)

# def get_file_creation_time(file_path):
#     creation_time = os.path.getctime(file_path)
#     return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(creation_time))

# creation_time = get_file_creation_time(mp3_file_path)
# print(f"File Creation Time: {creation_time}")

# def get_audio_duration(wav_file_path):
#     # Load the WAV file
#     samplerate, data = wavfile.read(wav_file_path)
#     # Calculate duration in seconds
#     duration = len(data) / samplerate
#     return duration

# def recognize_and_modify_text(wav_file_path, timestamps):
#     # Initialize recognizer
#     recognizer = sr.Recognizer()

#     # Get audio duration
#     audio_duration = get_audio_duration(wav_file_path)

#     # Load the entire audio file
#     with sr.AudioFile(wav_file_path) as source:
#         audio_data = recognizer.record(source)

#     # Use Google Web Speech API to recognize speech
#     try:
#         text = recognizer.recognize_google(audio_data, language='en-US')  # Adjust language if needed
#         print(f"Original Recognition Result: {text}")

#         # Convert the recognized text into a list of words
#         words = text.split()
#         total_words = len(words)

#         # Calculate approximate position of each timestamp in terms of word index
#         word_per_second = total_words / audio_duration
#         marker_positions = [int(timestamp * word_per_second) for timestamp in timestamps]

#         # Ensure positions are within the range of the text
#         marker_positions = [min(max(0, pos), total_words - 1) for pos in marker_positions]

#         # Modify text to include markers at specified positions
#         modified_text = []
#         current_index = 0

#         for i, word in enumerate(words):
#             if i in marker_positions:
#                 # Add marker before the current word
#                 modified_text.append(f"[image {timestamps[marker_positions.index(i)]}s]")
#             # Add the current word
#             modified_text.append(word)

#         # Join modified words into a single paragraph
#         final_text = ' '.join(modified_text)
#         print(f"Modified Recognition Result: {final_text}")

#     except sr.UnknownValueError:
#         print("Google Web Speech API Cannot Understand Audio")
#     except sr.RequestError as e:
#         print(f"Cannot gain result from Google Web Speech API: {e}")

# # Specify the times (in seconds) where you want to insert markers
# timestamps = [5, 15, 40]  # Times in seconds

# # Perform speech recognition and modify text
# recognize_and_modify_text(wav_output_path, timestamps)

from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def transcribe_audio_files(file_paths):
    transcriptions = []

    for file_path in file_paths:
        try:
            # Open the audio file
            with open(file_path, "rb") as audio_file:
                # Create a transcription using the Whisper model
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
                # Append the transcribed text to the results list
                transcriptions.append(transcription["text"])
        except Exception as e:
            print(f"Error transcribing {file_path}: {e}")
            transcriptions.append(None)

    return transcriptions


if __name__ == '__main__':
    audio_file = open("/home/yru2/HopHack24/voice2text/Matrix multiplication.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    print(transcription.text)
