# 🎵 Spotify Lyrics & Album Image Analytics Project

---

## **📌 Project Overview**

This project performs multi-modal analytics on three major artists:

- **Drake**
- **Taylor Swift**
- **The Weeknd**

The project combines:

- 🎵 Spotify API (album + song metadata)
- 📜 Genius API (lyrics extraction)
- 🖼 AWS Rekognition (album cover image analytics)
- 📊 NLP techniques (WordCloud, Lemmatization, Stemming)
- 💬 Sentiment Analysis (VADER + TextBlob)
- 🚫 Profanity Detection
- 🤖 Emotion Analysis (NRCLex + GenAI comparison)

The objective is to analyze how **lyrics, sentiment, emotions, profanity usage, and album visuals differ across artists**.

---

## **🛠 Technologies Used**

- Python
- Pandas
- Matplotlib
- WordCloud
- NLTK
- TextBlob
- VADER Sentiment Analyzer
- better_profanity
- NRCLex
- Spotipy (Spotify API)
- lyricsgenius (Genius API)
- AWS Rekognition

---

## **📂 Project Workflow**

---

## **Q1 – Spotify Data Extraction**

- Retrieved albums and songs using Spotify API
- Extracted:
  - Album Title
  - Album Cover URL
  - Artist Name
  - Song List
- Stored structured metadata in CSV format

---

## **Q2 – WordCloud & Text Normalization**

- Cleaned lyrics:
  - Removed punctuation
  - Removed brackets and metadata
  - Lowercased text
- Generated:
  - One WordCloud per artist
- Applied:
  - Lemmatization (WordNetLemmatizer)
  - Stemming (Porter Stemmer)
- Compared vocabulary differences across artists

---

## **Q3 – Sentiment Analysis**

Performed sentiment analysis using:

- **TextBlob**
- **VADER (Compound Score)**

For each artist calculated:

- Mean
- Standard Deviation
- Minimum
- Maximum

Generated trend diagrams showing compound score distribution per song.

---

## **Q4 – Image Analytics (AWS Rekognition)**

- Analyzed unique album covers only (to preserve AWS credits)
- Extracted top 3 high-confidence labels per image
- Compared image labels with:
  - Top 3 unigrams from album titles
- Evaluated alignment between visual themes and textual themes

---

## **Q5 – Profanity Analysis**

- Used `better_profanity` library
- Assigned binary profanity flag (1/0) per song
- Extracted explicit words used
- Calculated:
  - % of songs containing profanity
  - % of profane words per total words
- Compared profanity usage across artists

---

## **Q6 – Emotion Analysis (Lexicon vs GenAI)**

- Used **NRCLex** for lexicon-based emotion detection
- Compared results with contextual GenAI interpretation
- Evaluated differences between:
  - Dictionary-based emotion detection
  - Context-aware emotional understanding

---

## **📈 Key Insights**

- Drake shows highest profanity usage and sentiment volatility.
- Taylor Swift demonstrates higher average positive sentiment.
- The Weeknd displays strong emotional intensity with darker tonal patterns.
- Album visuals align most strongly with textual themes in The Weeknd’s discography.
- Lemmatization improves interpretability; stemming increases compression but reduces readability.

---

## **📁 Repository Contents**

- Jupyter Notebooks for each question (Q1–Q6)
- Processed analysis CSV outputs
- Image label datasets
- Sentiment and profanity results
- Emotion analysis outputs

(Note: Raw copyrighted lyrics are not included.)

---

## **🚀 How to Run**

1. Install required libraries:pip install pandas matplotlib nltk wordcloud textblob vaderSentiment better_profanity nrclex spotipy lyricsgenius boto3

2. 
2. Add your API credentials locally:
- Spotify Client ID
- Spotify Client Secret
- Genius API Key
- AWS Credentials

3. Run notebooks in order (Q1 → Q6).

---

## **📌 Conclusion**

This project demonstrates an end-to-end pipeline integrating:

- API data extraction
- Natural Language Processing
- Sentiment and emotion analytics
- Image recognition
- Comparative artist-level analysis

It showcases multi-modal analytics combining text and image intelligence within a unified framework.
