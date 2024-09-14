from moviepy.editor import AudioFileClip
import speech_recognition as sr
from datetime import datetime

# MP3 to WAV conversion using moviepy
mp3_file_path = r'/home/yru2/HopHack24/voice2text/Harry.mp3'
wav_output_path = r'/home/yru2/HopHack24/voice2text/WAV_AUDIO_FILE.wav'

# Record the current time (start time of recording)
start_time_real = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Recording Start Time: {start_time_real}")

# Load the MP3 file
audio_clip = AudioFileClip(mp3_file_path)

# Write the audio to WAV format
audio_clip.write_audiofile(wav_output_path, codec='pcm_s16le')

# Function to recognize audio
def recognize_audio(wav_file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Load audio from the WAV file
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)

    # Use Google Web Speech API to recognize speech
    try:
        text = recognizer.recognize_google(audio_data, language='en-US')  # Adjust language if needed
        print(f"Result of Recognition: {text}")
    except sr.UnknownValueError:
        print("Google Web Speech API Cannot Understand Audio")
    except sr.RequestError as e:
        print(f"Cannot gain result from Google Web Speech API: {e}")

# Example: Perform speech recognition on the converted WAV file
recognize_audio(wav_output_path)