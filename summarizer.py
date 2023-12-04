import extractive as etr
import textblob
import nltk
from textblob import TextBlob
from newspaper import Article


def get_summarized_text(text, type, lines):
    summary = text
    if type == 1:
        text = extract_article(text)
    summary = etr.generate_summary(text, top_n=lines)
    return summary


def extract_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
