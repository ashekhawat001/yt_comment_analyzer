## YouTube Video Comment Sentiment Analyzer

This project analyzes the sentiment of comments from YouTube videos using Python and various Natural Language Processing (NLP) libraries.

### Features

* Extracts comments from a YouTube video using the YouTube Data API v3.
* Preprocesses comment text using scikit-learn and NLTK libraries (tokenization, lemmatization, stop word removal, etc.).
* Analyzes sentiment of preprocessed comments using VADER, a lexicon-based sentiment analysis tool.
* Categorizes comments as positive, negative, or neutral.

### Dependencies

* Python 3.x
* `google-api-python-client`
* `scikit-learn`
* `nltk`
* `vaderSentiment`
* `matplotlib` (for visualization)
* `pandas` (for data manipulation)
* `numpy` (for numerical computations)
* `seaborn` (for enhanced visualizations)
* `spacy` (for advanced NLP tasks)
* **NLTK stopwords and tokenizers** (for more granular text pre-processing)
* **TfidfVectorizer and KMeans** (for potential topic modeling exploration)

### Instructions

1. **Install dependencies:**

   ```bash
    pip install google-api-python-client scikit-learn nltk vaderSentiment matplotlib pandas numpy seaborn spacy

   ```

2. **Create a YouTube API project and obtain credentials:**

   [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)

   * Enable the YouTube Data API v3 for your project.
   * Download your API credentials (KEY).

3. **Configure API credentials:**
    Save this key in a Seperate file or using
   ```bash
   export YOUR_API_KEY= API_KEY
   ```

   and then in python
   ```python
   import os
   api_key = os.environ.get('YOUR_API_KEY')
   # Use the API key here
   ```
   

5. **Run the script:**

   ```bash
   python yt_public.py <VIDEO_ID>
   ```

   Replace `<VIDEO_ID>` with the YouTube video ID you want to analyze.

**Example:**

```bash
python yt_public.py dQw4w9WgXcQ
```

This will analyze the comments for the video with ID "dQw4w9WgXcQ" (you know what it is...).

### Output

The script will generate a CSV file named `comments_dQw4w9WgXcQ_'today'.csv` containing the following columns:

* `comment_text`: The original text of the comment.
* `likes`: number of likes on that comment

A visualization (e.g., pie chart) depicting the distribution of positive, negative, and neutral comments.

### Further Development

This is a basic project and can be extended in various ways:

* Implement more sophisticated NLP techniques for pre-processing and sentiment analysis.
* Explore different sentiment analysis models (e.g., machine learning models).
* Visualize the sentiment distribution of the comments.
* Analyze other aspects of the comments, such as topic modeling.

