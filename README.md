# finbert_finviz

## Financial News Sentiment Analysis 

Financial News Sentiment Analysis utilizes finBERT model from hugging face library to perform realtime sentiment analysis of news headlines published on FinViz.com.

`get_latest_news()` function in `scraper.py` scrapes news headlines using beautifulsoup library. The streamlit web application is programmed in `app.py` and performs sentiment analysis by importing `finBERT` model and tokenizer.

`requirements.txt` has all the libraries and their versions this application depends upon.

The web application is hosted on Spaces by Huggingface.
App: [https://finsenanalysis.streamlit.app/](https://huggingface.co/spaces/sushobhan55/finbert_finviz)https://huggingface.co/spaces/sushobhan55/finbert_finviz
