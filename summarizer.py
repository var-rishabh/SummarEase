# Import necessary libraries and modules
import textblob
import nltk
from textblob import TextBlob
from newspaper import Article

# Assuming this is a custom module for extractive summarization
import extractive as etr


# Function to extract the text content from a given URL
def extract_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text


# Function to get a summarized version of the input text
def get_summarized_text(text, summarizeType, length):
    summary = text
    # If summarizeType is 1, assume the input is a URL and extract the article text
    if summarizeType == 1:
        text = extract_article(text)

    summary = etr.generate_summary(text, top_n=length)
    return summary
