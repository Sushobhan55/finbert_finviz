# streamlit app

import streamlit as st
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline
from scraper import get_latest_news

# Load FinBERT model and tokenizer
finbert = BertForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone", num_labels=3)
tokenizer = BertTokenizer.from_pretrained("yiyanghkust/finbert-tone")

# Create sentiment analysis pipeline
nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    results = nlp(text)
    sentiment_label = results[0]["label"]
    return sentiment_label

# Function to get sentiment labels for a list of headlines
def get_sentiment_labels(headlines_list):
    sentiment_labels = []
    for headline in headlines_list:
        label = analyze_sentiment(headline)
        sentiment_labels.append(label)
    return sentiment_labels

# Function to print a Streamlit table with news headlines and sentiment labels
def display_news_sentiment_table(headlines_list, sentiment_labels):
    df = pd.DataFrame({
        "Headlines": headlines_list,
        "Sentiment": sentiment_labels
    })

    # Function to apply background colors based on sentiment labels
    def style_func(val):
        color_dict = {
            "negative": 'red',
            "positive": 'green',
            "neutral": 'gray'
        }
        return f"background-color: {color_dict[val.lower()]}"

    # Display the table
    st.dataframe(df.set_index("Headlines").style.applymap(style_func, subset=["Sentiment"]))

# Streamlit app
st.title("Financial News Sentiment Analysis")

# Get the latest news headlines and sentiment labels using the scraper
latest_news_headlines = get_latest_news()
sentiment_labels = get_sentiment_labels(latest_news_headlines)

# Display the table in the Streamlit app
display_news_sentiment_table(latest_news_headlines, sentiment_labels)

# Refresh button
if st.button("Refresh"):
    st.experimental_rerun()

# App Description
st.markdown("---")
st.subheader("Description")
st.info("This app uses the [FinBERT](https://huggingface.co/yiyanghkust/finbert-tone) model from Hugging Face to perform sentiment analysis on financial news headlines. The headlines are scraped in real-time from [Finviz](https://finviz.com/). The news headlines displayed on the web app are the latest, and you can click the 'Refresh' button to update the headlines and sentiment analysis.")
st.markdown("---")