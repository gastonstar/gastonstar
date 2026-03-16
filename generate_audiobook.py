import os
import sys
import time
from gtts import gTTS

def generate_audiobook(story_text, output_directory="audiobooks"):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    # Construct the output file path
    output_file = os.path.join(output_directory, "tommy_rescate.mp3")

    try:
        print("Generating audio, please wait...")
        # Generate audio from text
        tts = gTTS(text=story_text, lang='en')
        tts.save(output_file)

        print(f"Audio generated successfully: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Sample Tommy Rescate story text
    story_text = (
        "Once upon a time in a faraway land, there lived a brave young boy named Tommy. "
        "Tommy loved adventures and dreamed of exploring the world beyond his village. "
        "One day, he decided to embark on a journey to find treasures hidden deep within the enchanted forest..."
        # Add more story content as needed
    )

    generate_audiobook(story_text)