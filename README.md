# 🎥 Communication Analysis Tool for Human-AI Interaction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![First Contribution](https://img.shields.io/badge/First%20Open%20Source%20Contribution-Yes-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This tool analyzes speech-based communication in driving simulator experiments. It converts video to audio, transcribes speech, performs sentiment analysis, and visualizes the emotional distribution. It’s designed to help understand how AI can interpret and respond to human emotions in driving simulations.

---

## 📁 Project Files

| File Name                  | Description |
|---------------------------|-------------|
| `conversion_to_mp3.py`    | Extracts and segments audio from a video using `mediapy`. Chunks are 5 seconds each. |
| `audio_to_speech.py`      | Transcribes audio chunks using OpenAI’s Whisper. Empty audios return `null`. |
| `speech_to_sentimental.py`| Analyzes sentiment using Hugging Face's pipeline. Saves output as a CSV. |
| `visualize.py`            | Generates bar plots to visualize sentiment confidence and distribution. |

---

## 📊 Example Output

### CSV Columns
- `filename`
- `transcription`
- `sentiment` *(POSITIVE, NEGATIVE, NEUTRAL)*
- `confidence` *(model prediction score or NA)*

### Visuals
- 📈 **Average Confidence per Sentiment**
- 📊 **Count of Each Sentiment (incl. NEUTRAL/null)**

---

## 🔧 Requirements

```bash
pip install pandas matplotlib seaborn openai-whisper transformers torchaudio mediapy opencv-python
