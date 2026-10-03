from flask import Flask, render_template, request
import joblib
import re
import nltk
import os

# Initialize the Flask app
app = Flask(__name__)

# Download the required NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Load your pre-trained model and TfidfVectorizer
model = joblib.load('model/sentiment_model.pkl')
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')

# Preprocessing functions
def clean_text(text):
    # Remove special characters
    def remove_special_characters(text):
        pattern = r'[^a-zA-Z0-9\s]'
        return re.sub(pattern, '', text)

    # Remove stopwords
    def remove_stopwords(text):
        stopword_list = nltk.corpus.stopwords.words('english')
        tokens = text.split()
        filtered_tokens = [token for token in tokens if token not in stopword_list]
        filtered_text = ' '.join(filtered_tokens)
        return filtered_text

    # Apply stemming
    def simple_stemmer(text):
        ps = nltk.porter.PorterStemmer()
        return ' '.join([ps.stem(word) for word in text.split()])

    text = remove_special_characters(text)
    text = simple_stemmer(text)
    text = remove_stopwords(text)
    return text

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for predicting sentiment
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input text from the form
        text = request.form['text']
        
        # Preprocess the input text
        cleaned_text = clean_text(text)
        
        # Transform the text using TfidfVectorizer
        vectorized_text = vectorizer.transform([cleaned_text])
        
        # Predict sentiment
        prediction = model.predict(vectorized_text)[0]
        
        # Map prediction result to human-readable output
        sentiment = "Positive" if prediction == 1 else "Negative"
        
        return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)