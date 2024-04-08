# Working with Dataframes
import numpy as np
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Word Tokenization
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

# Data Sciency Stuff
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


dtype_specification = {'Likes':'int',
                       'Comments':'int', 
                       'Views':'int',
                       'Keyword':'category'}
comments = pd.read_csv("comments_MTe12fH2xtQ_09-04-2024.csv")



# For the sake of this project, the Sentiment column needs to be dropped
#comments.drop(columns=['Unnamed: 0', 'Sentiment'], inplace=True)

# Adjust columns

# Display the datasets
#print(video_statistics)
print(comments)


def preprocess_text(comments):
    # Create empty list
    preprocessed_comments = []
    # Initiate Tokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    # Get word stems for better results
    stemmer = PorterStemmer()
    # Take out words that are too common
    stop_words = set(stopwords.words('english'))

    for comment in comments:
        # Tokenize each comment and change all words to lowercase
        tokens = tokenizer.tokenize(comment.lower())
        # Filter words against too common words
        filtered_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
        # Append to empty string
        preprocessed_comments.append(' '.join(filtered_tokens))
    
    return preprocessed_comments

def analyze_sentiment(comments):
    # Initiate Sentiment Analyzer
    sia = SentimentIntensityAnalyzer()
    # Create empty list
    sentiment_scores = []

    for comment in comments:
        # Apply a score to each comment
        sentiment_score = sia.polarity_scores(comment)
        sentiment_scores.append(sentiment_score)
    
    return sentiment_scores

def visualize_sentiment(sentiment_scores):
    compound_scores = [score['compound'] for score in sentiment_scores]
    positive_count = sum(1 for score in compound_scores if score > 0)
    negative_count = sum(1 for score in compound_scores if score < 0)
    neutral_count = sum(1 for score in compound_scores if score == 0)

    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive_count, negative_count, neutral_count]
    colors = ['#66c2a5', '#fc8d62', '#8da0cb']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Comment Sentiment Distribution')
    plt.show()


# First, we need to match the comments to their videos and the video categories
#merged_comments = comments.merge(video_statistics[['Video ID','Keyword', 'Title']], on='Video ID',how='inner')

# Using my random video selector
video_comments = (comments)

# Display the video title and the comments associated to it
print(video_comments)

# Preprocess comments
preprocessed_comments = preprocess_text(video_comments)

# Analyze sentiment scores for the video
sentiment_scores = analyze_sentiment(preprocessed_comments)

visualize_sentiment(sentiment_scores)

