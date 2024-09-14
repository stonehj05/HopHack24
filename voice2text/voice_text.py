from moviepy.editor import AudioFileClip
import speech_recognition as sr

# MP3 to WAV conversion using moviepy
mp3_file_path = r'/Users/ruyutong/Desktop/Harry.mp3'
wav_output_path = r'/Users/ruyutong/Desktop/file1.wav'

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