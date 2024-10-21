# /src/ai/models/sentiment_analysis.py

from transformers import pipeline

class SentimentAnalysis:
    """
    Sentiment Analysis model for analyzing market sentiment from news and social media.
    Uses a pre-trained model from the Hugging Face 'transformers' library.
    """

    def __init__(self):
        # Initialize the sentiment analysis pipeline
        self.sentiment_pipeline = pipeline('sentiment-analysis')

    def analyze_text(self, text):
        """
        Analyzes the sentiment of a given text (e.g., news articles, social media posts).
        """
        sentiment = self.sentiment_pipeline(text)
        return sentiment

    def get_sentiment_score(self, market_news):
        """
        Analyzes the sentiment of market news and returns a sentiment score.
        Positive sentiment returns a positive score; negative sentiment returns a negative score.
        """
        sentiment = self.analyze_text(market_news)
        return sentiment[0]['score'] if sentiment[0]['label'] == 'POSITIVE' else -sentiment[0]['score']
