# Sentiment Analysis Web Application

A Flask-based web application that uses Natural Language Processing (NLP) and Machine Learning to classify English text as **Positive** or **Negative**.

## Project Overview

This project demonstrates an end-to-end sentiment analysis workflow:

1. User enters English text through the web interface.
2. The text is cleaned using NLP preprocessing techniques.
3. Stopwords are removed and words are stemmed using Porter Stemmer.
4. The processed text is converted into numerical features using TF-IDF.
5. A pre-trained Machine Learning model predicts the sentiment.
6. The result is displayed as **Positive** or **Negative**.

The application is built with **Python Flask** and provides a simple responsive web interface.

## Features

- Positive and Negative sentiment classification
- NLP-based text preprocessing
- Special-character removal
- Stopword removal
- Porter stemming
- TF-IDF feature extraction
- Pre-trained Machine Learning model
- Simple responsive web interface
- Real-time prediction through the Flask application

## Technologies Used

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Machine Learning & NLP
- NLTK
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Joblib

## Project Structure

```text
Sentiment-Analysis-Flask/
│
├── Data/
│   └── Train.csv
│
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── screen_sh/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── nlp_analyse_des_sentiments.py
├── NLP_Analyse_des_sentiments.ipynb
├── requirements.txt
├── .gitignore
└── README.md