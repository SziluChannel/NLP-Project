import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import re
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup



    
def AI(model, vectorizer, input):

    if model == "nn": 
        ext = "keras" 
    elif model == "lr": 
        ext = "pkl"
    else:
        raise Exception("Invalid model type")

    model_name = format(f"models/{model}_{vectorizer}.{ext}")
    print(model_name)
    # Load the trained model
    if model=="nn":
        loadedmodel = tf.keras.models.load_model(model_name)
    elif model=="lr":
        loadedmodel = joblib.load(model_name)
    # Load the saved vectorizer
    vectorizer = joblib.load(format(f'models/{vectorizer}.pkl'))

    # Initialize the stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    def stem_and_lemmatize(text):
        words = text.split()
        stemmed_words = [stemmer.stem(word) for word in words]
        lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]
        return " ".join(lemmatized_words)

    def clean_text_advanced(text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
        text = text.strip()
        text = BeautifulSoup(text, "html.parser").get_text() # Remove HTML tags
        stop_words = set(stopwords.words('english'))
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        text = " ".join(filtered_words)

    # Preprocess the user input
    user_input = clean_text_advanced(input)
    user_input = stem_and_lemmatize(input)
    user_input_vec = vectorizer.transform([input])
    print("\n\n\n\n")
    # Make a prediction
    prediction = loadedmodel.predict(user_input_vec)
    predicted_class = np.argmax(prediction)  # Use argmax for multi-class

    print("Predicted class:", predicted_class)
    print(prediction)
    if predicted_class == 0:
        return "Fake"
    elif predicted_class==1:
        return "True"
    raise Exception("Invalid prediction")