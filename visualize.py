import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("transcription_sentiments.csv")
# Count plot of Sentiment Types
# Replace nulls in sentiment with 'NEUTRAL' for counting
df_count = df.copy()
df_count['sentiment'] = df_count['sentiment'].fillna("NEUTRAL")

plt.figure(figsize=(6, 5))

# Countplot of sentiment types
sns.barplot(
    x=df_count['sentiment'].value_counts().index,
    y=df_count['sentiment'].value_counts().values,
    palette={"POSITIVE": "green", "NEGATIVE": "red", "NEUTRAL": "gray"}
)

plt.title("Sentiment Occurrence Count", fontsize=15)
plt.xlabel("Sentiment Type", fontsize=12)
plt.ylabel("Number of Audio Segments", fontsize=12)
plt.tight_layout()
plt.savefig("sentiment_occurrence_plot.png")
plt.show()
