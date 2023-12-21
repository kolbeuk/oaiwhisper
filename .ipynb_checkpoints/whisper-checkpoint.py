#!/usr/bin/env python
# coding: utf-8

import concurrent.futures
import sys
import whisper

def transcribe_video(filename, model):
    try:
        print(f"Transcribing video: {filename}")
        result = model.transcribe(filename)

        # Create a valid filename for the transcription
        transcript_filename = f"{filename}.txt".replace('/', '_').replace('\\', '_').replace(' ', '_')

        # Write the transcription to a file
        with open(transcript_filename, 'w') as file:
            file.write(result['text'])
        
        print(f"Transcription saved to '{transcript_filename}'")
    except Exception as e:
        print(f"Error during transcription: {e}")

def main(filenames, model):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        # Pass the model as an argument to each invocation of transcribe_video
        executor.map(lambda file: transcribe_video(file, model), filenames)

if __name__ == "__main__":
    # Assuming file paths are passed as separate command-line arguments
    filenames = sys.argv[1:]
    
    # Load the Whisper model
    model = whisper.load_model("tiny")
    print("Whisper model loaded.")
    
    main(filenames, model)
