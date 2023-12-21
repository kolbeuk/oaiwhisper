#!/usr/bin/env python
# coding: utf-8

import concurrent.futures
import sys
import whisper
import datetime

def transcribe_video(filename):
    try:   
        # Load the Whisper model
        model = whisper.load_model("tiny")
        print("Whisper model loaded.")
        current_time = datetime.datetime.now().time()

        print(current_time)
        print(f"Transcribing video: {filename} at {current_time}")
        result = model.transcribe(filename, fp16=False)

        current_time = datetime.datetime.now().time()
        print(f"Completed Transcribing video: {filename} at {current_time}")
        # Create a valid filename for the transcription
        transcript_filename = f"{filename}.txt".replace('/', '_').replace('\\', '_').replace(' ', '_')

        # Write the transcription to a file
        with open(transcript_filename, 'w') as file:
            file.write(result['text'])
        
        print(f"Transcription saved to '{transcript_filename}' at {current_time}")
    except Exception as e:
        print(f"Error during transcription: {e}")

def main(filenames):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        # Pass the model as an argument to each invocation of transcribe_video
        executor.map(lambda file: transcribe_video(file), filenames)

if __name__ == "__main__":
    # Assuming file paths are passed as separate command-line arguments
    filenames = sys.argv[1:]
    main(filenames)