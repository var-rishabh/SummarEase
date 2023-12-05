import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

nltk.download("punkt")
nltk.download("stopwords")


def preprocess_text(text):
    # Tokenize the text into sentences and words, remove stopwords, and normalize the words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sent.lower()) for sent in sentences]
    stop_words = set(stopwords.words("english"))
    words = [[word for word in words if word not in stop_words] for words in words]
    return sentences, words


def sentence_similarity(sent1, sent2):
    # Calculate cosine similarity between two sentences based on words
    vector1 = [word.lower() for word in sent1]
    vector2 = [word.lower() for word in sent2]

    all_words = list(set(vector1 + vector2))
    vector1_count = {word: 0 for word in all_words}
    vector2_count = {word: 0 for word in all_words}

    for word in vector1:
        vector1_count[word] += 1

    for word in vector2:
        vector2_count[word] += 1

    vector1 = [count for count in vector1_count.values()]
    vector2 = [count for count in vector2_count.values()]

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, words):
    # Build similarity matrix between sentences
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(words[i], words[j])

    return similarity_matrix


def generate_summary(text, top_n=5):
    sentences, words = preprocess_text(text)
    sentence_similarity_matrix = build_similarity_matrix(sentences, words)

    # Create graph from similarity matrix
    graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(graph)

    # Sort sentences by their scores
    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True
    )

    # Extract top sentences as summary
    summary = " ".join([sentence for score, sentence in ranked_sentences[:top_n]])
    return summary
