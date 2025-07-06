# 📱 Sentiment Analysis on Apple iPhone 11 Reviews and Social Media Updates/Comments

## 🧾 Introduction
This project performs a comprehensive sentiment analysis on Apple iPhone 11 customer reviews and Social Media Updates. It leverages multiple sentiment analysis techniques, including TextBlob, VADER, RoBERTa, and Zero-Shot Classification, to evaluate the sentiment polarity of reviews. The goal is to compare these models against user-provided ratings and extract meaningful insights about customer opinions.

The project also includes text preprocessing, data cleaning, visualisation (word clouds, rating distributions, confusion matrices), n-gram analysis, and emotion detection using the GoEmotions model to capture nuanced emotional states from the reviews and other NLP models, revealing platform, hashtag, and temporal patterns in user sentiment.

## 📁 Repository Structure

```plaintext
Sentimental-Analysis/
│
├── 📂 data/
│   ├── apple_iphone_11_reviews.csv            # Product reviews dataset
│   └── social_media_posts.csv                 # Collected social media posts (Twitter/X, Facebook, Instagram)
│
├── 📄 iPhone11_Sentiment_Analysis.ipynb       # Iphone 11 reviews analysis
├── 📄 Social Media Sentiment Analysis.ipynb   # Social Media posts analysis
├── 📄 TextCleaner.py                          # Ad-Hoc class used to clean text
├── 📄 Model Explanation.png                   # Sentimental Model description
└── 📄 README.md                               # Project overview and methodology

```

## 🔧 Key Components and Files

- **Sentiment analysis** using:
  - TextBlob (polarity and subjectivity)
  - VADER (lexicon-based sentiment scoring)
  - RoBERTa (transformer-based sentiment classification)
  - Zero-Shot Classification (using BART-large-MNLI model)
- **Data cleaning and preprocessing** with custom text cleaning and stopword removal.
- **Exploratory Data Analysis (EDA)** including rating distributions and review helpfulness.
- **Visualisation** tools: seaborn, matplotlib, and word clouds.
- **Emotion Detection** using BERT-based GoEmotions multi-label classifier.
- **N-gram frequency analysis** for top unigrams, bigrams, and trigrams.
- **Disagreement analysis** to identify reviews with sentiment rating conflicts across models.
- **Top positive and negative word/sentence extraction** based on VADER scoring.

## 📌 Methodology

### 🔍 Data Loading
- Load review data and user ratings from the CSV file.

### 🧹 Data Cleaning
- Removal of duplicates and missing values.
- Custom text cleaning using the `TextCleaner` class to:
  - Normalize unicode characters and remove accents.
  - Replace URLs, HTML tags, user mentions, numbers, and alphanumeric tokens with placeholders.
  - Optionally remove non-ASCII characters and control currency symbol retention.
  - Remove stopwords and product-specific/custom keywords.
  - Apply lemmatization to reduce words to their root forms.

### 📊 Exploratory Data Analysis
- Visualise rating distributions.
- Analyse helpful counts and comment statistics by rating groups.
- Generate word clouds from cleaned review text and analysis.

### 💬 Sentiment Analysis
- Apply multiple sentiment models (TextBlob, VADER, Roberta, Zero-Shot) to assign sentiment scores and ratings.
- Map polarity/score ranges to sentiment categories (Negative, Neutral, Positive).
- Compare model predictions with user ratings using confusion matrices and MAE (Mean Absolute Error).

### 😊 Emotion Detection
- Utilise the GoEmotions BERT-based model to categorise the dominant emotions in reviews.
- Visualise the most common emotions.

### 🔠 N-Gram Analysis
- Extract and plot the top 1, 2, and 3-grams from review texts.

### ⚖️ Disagreement Detection
- Identify reviews where sentiment ratings from different models diverge significantly.
- Flag inconsistencies for further review.

### 📊 Output & Results

- 📉 **Emotion Bar Charts** – Visualise the distribution of detected emotions across social media posts.
- 🕒 **Temporal Trend Graphs** – Track sentiment and emotion changes over time (if timestamps are available).
- ☁️ **Platform-Specific Word Clouds** – Highlight common terms across platforms like Twitter/X.
- 🤖 **Model Comparison** – Contrast sentiment predictions across TextBlob, VADER, RoBERTa, and Zero-Shot models.
- 🧹 **Cleaned & Annotated Datasets** – Includes reviews and social posts with sentiment scores and dominant emotions.
- 📍 **Sentiment Divergence by Platform** – Reveal inconsistencies in sentiment between product reviews and social media.
- 📈 **Visual Summaries** – Showcase top emotions, sentiment polarity spread, and key textual patterns.

## 🧠 Key Insights

- Social media sentiment often diverges from product review sentiment, especially around launch events or price changes.
- VADER and TextBlob sometimes underestimate emotional intensity compared to transformer-based models, such as RoBERTa.
- Common emotions include *joy*, *approval*, and *annoyance*; these vary by platform and user demographic.

## 🔮 Future Enhancements

- Integrate live sentiment tracking via Twitter API.
- Expand analysis to other Apple devices for comparison.
- Fine-tune transformer models for product-specific sentiment detection.
- Developed classification models (Naive Bayes, Logistic Regression, Random Forest, etc.) to predict sentiment categories based on preprocessed reviews and social media text.

## 📦Dependencies
This project uses several Python packages and libraries, including:

* numpy
* pandas
* scikit-learn
* matplotlib
* seaborn
* wordcloud
* nltk
* spacy
* textblob
* vaderSentiment
* transformers
* torch
* tensorflow
* sentencepiece
* emoji
* plotly
* jupyter
