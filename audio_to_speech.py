import whisper
import os

model = whisper.load_model("base")  # Load the Whisper model

audio_folder = "audio_chunks" # Folder containing audio files
output_folder = "transcriptions" # Folder to save transcriptions

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the audio folder
for filename in sorted(os.listdir(audio_folder)):
    if filename.endswith(".mp3"):
        audio_path = os.path.join(audio_folder, filename)
        result = model.transcribe(audio_path, language="en")

        # Save transcription to a text file
        output_file = os.path.join(output_folder, f"{filename[:-4]}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"{filename} → {result['text']}")
