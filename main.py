import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

a = input("Audio File Path:")

def remove_dead_space(input_file, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Detect silence and split audio into segments
    segments = split_on_silence(audio, min_silence_len=60, silence_thresh=-45)

    # Combine non-silent segments into a single audio file
    output = AudioSegment.silent()
    for segment in segments:
        output += segment

    # Export the modified audio
    output.export(output_file, format="wav")

# Use the uploaded file path
input_file = a  # Replace with the name of the uploaded file
output_file = "output_audio.wav"

# Check if input file exists
if os.path.exists(input_file):
    remove_dead_space(input_file, output_file)
    print("Dead space removed. Output saved as 'output_audio.wav'.")
else:
    print("Input file not found. Please make sure the file path is correct.")
