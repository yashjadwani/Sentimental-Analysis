# 📱 Sentiment Analysis on Apple iPhone 11 Reviews

## 🧾 Introduction
This project performs a comprehensive sentiment analysis on Apple iPhone 11 customer reviews. It leverages multiple sentiment analysis techniques, including TextBlob, VADER, RoBERTa, and Zero-Shot Classification, to evaluate the sentiment polarity of reviews. The goal is to compare these models against user-provided ratings and extract meaningful insights about customer opinions.

The project also includes text preprocessing, data cleaning, visualisation (word clouds, rating distributions, confusion matrices), n-gram analysis, and emotion detection using the GoEmotions model to capture nuanced emotional states from the reviews.

## 📁 Repository Structure

- **Data** - Contains the Apple iPhone 11 reviews dataset (`apple_iphone_11_reviews.csv`).
- **Scripts/Notebooks** - Jupyter notebooks or scripts containing the analysis pipeline.
- **Visualisations** - Generated plots such as word clouds, histograms, heatmaps, and bar charts.

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
- Dataset loaded from CSV containing iPhone 11 reviews and ratings.

### 🧹 Data Cleaning
- Removal of duplicates and missing values.
- Custom text cleaning to remove non-ASCII characters and product-specific keywords.
- Stopword removal and lemmatisation preparation.

### 📊 Exploratory Data Analysis
- Visualise rating distributions.
- Analyse helpful counts and comment statistics by rating groups.
- Generate word clouds from cleaned review text.

### 💬 Sentiment Analysis
- Apply multiple sentiment models (TextBlob, VADER, RoBERTa, Zero-Shot) to assign sentiment scores and ratings.
- Map polarity/score ranges to sentiment categories (Negative, Neutral, Positive).
- Compare model predictions with user ratings using confusion matrices and MAE (Mean Absolute Error).

### 😊 Emotion Detection
- Utilise the GoEmotions BERT-based model to categorise the dominant emotions in reviews.
- Visualise the most common emotions.

### 🔠 N-Gram Analysis
- Extract and plot the top 1, 2, and 3-grams from review texts.

### ⚖️ Disagreement Detection
- Identify reviews where sentiment ratings from different models diverge significantly.

### 📈 Visualization
- Histograms, bar charts, heatmaps, and word clouds to summarise findings and model performance.


