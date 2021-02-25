import streamlit as st
from model import predict
import tensorflow as tf
import pickle

result = None

st.write('''# 🎬Movie Review System
Movie Review System is based on the Natural Processing Language or NLP Model
that takes the review from the user and predict the review as a `positive` or `negative`.
Model is train using the TensorFlow and TensorFlow API called Keras. This application predict 
the output with the accuracy level i.e. how much confident the model is on that particular prediction.

**You can check the notebook [here](https://github.com/abhishekv5055/movie-review-system/blob/main/Movie_Review_System.ipynb)**
''')

review = st.text_input('Write your review...')
button = st.button('Predict')
if button:
    if review:
        result, accuracy = predict(review)
        st.write(f'''**Prediction:** {result}''')
        st.write(f'''**Accuracy:** {accuracy:.2f}%''')
    else:
        st.write('Please enter the review...')

st.write('''
''')