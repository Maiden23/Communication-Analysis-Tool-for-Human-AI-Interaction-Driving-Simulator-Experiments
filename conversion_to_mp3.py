import moviepy
import os

video_path = "C:/Users/angel/OneDrive/Desktop/GSOC/Experimenter_CREW_999_1_All_1731617801.mp4"
video = moviepy.VideoFileClip(video_path)
duration = int(video.duration)  # Get the duration of the video in seconds and then convert float to integers

# Output folder
output_folder = "audio_chunks"
os.makedirs(output_folder, exist_ok=True) # Checks if the folder exists so that it doesnt create a new one

# Using loops to Split into 5-second audio chuncks
for i in range(0, duration, 5):
    start = i
    end = min(i + 5, duration)  # to avoid exceeding the video's duration
    chunk = video.subclipped(start, end)  # Create a subclip of 5 seconds 
    audio = chunk.audio
    output_path = os.path.join(output_folder, f"chunk_{start}_{end}.mp3") 
    audio.write_audiofile(output_path)
    print(f"Saved: {output_path}")

video.close()
print("All 5-second audio chunks created!")