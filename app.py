import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Paths to your downloaded files
model_path = "models/model.h5"
tokenizer_path = "models/tokenizer.pkl"

# Load the model
model = load_model(model_path)

# Load the tokenizer
with open(tokenizer_path, 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# predict sentiment
def predict_sentiment(text, maxlen=100):
    # Preprocess the input text
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=maxlen)
    
    # Make a prediction
    prediction = model.predict(padded_sequence)
    sentiment = 'positive' if prediction[0][0] >= 0.5 else 'negative'
    
    return sentiment

# Create the Streamlit user interface
st.title("Sentiment Analysis")

# Add user input
user_input = st.text_input("Enter text for sentiment analysis:")

if st.button("Analyze"):
    if user_input:  # Check if input is not empty
        sentiment = predict_sentiment(user_input)
        st.write(f"The sentiment of the text is: **{sentiment}**")
    else:
        st.write("Please enter some text to analyze.")
