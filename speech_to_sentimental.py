from transformers import pipeline
import pandas as pd
import os

# Load the sentiment analysis pipeline once
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Folder with transcription .txt files
transcription_folder = "transcriptions"
all_results = []

# Loop through each file
for filename in sorted(os.listdir(transcription_folder)):
    if filename.endswith(".txt"):
        file_path = os.path.join(transcription_folder, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()

        # Handle empty files
        if not text:
            sentiment_result = {"label": "N/A", "score": 0.0}
        else:
            sentiment_result = sentiment_pipeline(text)[0]

        # Collect all results in a single list
        all_results.append({
            "filename": filename,
            "transcription": text,
            "sentiment": sentiment_result["label"],
            "confidence": sentiment_result["score"]
        })

        print(f"Processed: {filename} → {sentiment_result}")

# Save all results into a single CSV file
df = pd.DataFrame(all_results)
df.to_csv("transcription_sentiments.csv", index=False)
print(" All the sentiment results saved to 'transcription_sentiments.csv'")
