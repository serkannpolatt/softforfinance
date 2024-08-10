import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt
import streamlit as st


def analyze_market_sentiment(symbol):
    # Lista de URLs de diferentes fuentes financieras
    urls = [
        f"https://finance.yahoo.com/quote/{symbol}/news",
        f"https://www.marketwatch.com/investing/stock/{symbol}/news",
        # Agrega aquí más URLs de otras fuentes financieras que desees analizar
    ]

    sentiment_scores = []

    for url in urls:
        # Realizar solicitud GET a la URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar titulares de noticias
        headlines = soup.find_all("h3")

        # Analizar el sentimiento de cada titular de noticia
        for headline in headlines:
            headline_text = headline.get_text()
            sentiment = TextBlob(headline_text).sentiment.polarity
            sentiment_scores.append(sentiment)

    # Calcular el sentimiento promedio del mercado
    if sentiment_scores:
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        avg_sentiment_rounded = round(avg_sentiment, 2)

        return avg_sentiment_rounded
    else:
        return None


analyze_market_sentiment(symbol="AMZN")
