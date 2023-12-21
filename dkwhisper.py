#!/usr/bin/env python
# coding: utf-8

import concurrent.futures
import sys
import whisper

def transcribe_video(filename):
    try:   
        # Load the Whisper model
        model = whisper.load_model("tiny")
        print("Whisper model loaded.")
    
        print(f"Transcribing video: {filename}")
        result = model.transcribe(filename, fp16=False)

        # Create a valid filename for the transcription
        transcript_filename = f"{filename}.txt".replace('/', '_').replace('\\', '_').replace(' ', '_')

        # Write the transcription to a file
        with open(transcript_filename, 'w') as file:
            file.write(result['text'])
        
        print(f"Transcription saved to '{transcript_filename}'")
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
