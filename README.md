# Sentiment Analysis Web Application

A web-based Sentiment Analysis application that uses Natural Language Processing (NLP) and Machine Learning to classify text as **Positive** or **Negative**.

## Project Overview

This project analyzes the sentiment expressed in a given piece of English text. The application preprocesses the input using NLP techniques, converts the cleaned text into numerical TF-IDF features, and uses a trained Machine Learning classification model to predict the sentiment.

The application provides a simple web interface built with HTML and CSS and is powered by a Python Flask backend.

## Features

- Positive and Negative sentiment classification
- Text preprocessing using NLP techniques
- Stopword removal
- Special-character removal
- Stemming using Porter Stemmer
- TF-IDF based text feature extraction
- Machine Learning based prediction
- Simple and responsive web interface
- Real-time sentiment prediction
- Example inputs for quick testing

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

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
└── README.md