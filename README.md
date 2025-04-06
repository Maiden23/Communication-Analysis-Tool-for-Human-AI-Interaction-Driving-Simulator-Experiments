# Communication Analysis Tool for Human-AI Interaction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)


This code analyzes speech-based communication in driving simulator experiments. Which converts video to audio, transcribes speech, performs sentiment analysis , and visualizes the emotional distribution. It’s designed to help understand how AI can interpret and respond to human emotions in driving simulations.

---

## Project Files

| File Name                  | Description |
|---------------------------|-------------|
| `conversion_to_mp3.py`    | Extracts and segments audio from a video using `mediapy`. Chunks are 5 seconds each. |
| `audio_to_speech.py`      | Transcribes audio chunks using OpenAI’s Whisper. Empty audios return `null`. |
| `speech_to_sentimental.py`| Analyzes sentiment using Hugging Face's pipeline. Saves output as a CSV. |
| `visualize.py`            | Generates bar plots to visualize sentiment confidence and distribution. |

---


### CSV Columns
- `filename`
- `transcription`
- `sentiment` *(POSITIVE, NEGATIVE, NEUTRAL)*
- `confidence` *(model prediction score or NA)*

### Visual
- **Count of Each Sentiment (incl. NEUTRAL/null)**
![image](https://github.com/user-attachments/assets/47e40d9b-40c3-4843-9a95-f6becad6fe18)

---

##  Requirements

```bash
pip install pandas matplotlib seaborn openai-whisper transformers torchaudio mediapy opencv-python

```
---

### How to run the code

-  The conversion_to_mp3.py : Converts input video files to .mp3 audio format.
- audio_to_speech.py : Transcribes the .mp3 audio using OpenAI Whisper.
- speech_to_sentimental.py : Performs sentiment analysis on the transcribed text using transformers.
- visualize.py : Generates sentiment visualization plots using the results using seaborn.

