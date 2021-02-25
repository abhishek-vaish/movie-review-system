import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

model = tf.keras.models.load_model('../nlp_model.h5')
tokenizer = pickle.load(open('../tokenizer.pkl', 'rb'))
MAXLEN=200
true_target = ['positive', 'negative']

def predict(review):
    data_list = []
    data_list.append(review)
    padding = data_manipulation(data_list)
    preds = model.predict(padding)
    result = true_target[np.argmax(preds)]
    return result

def data_manipulation(review_list, tokenizer=tokenizer):
    sequence = tokenizer.texts_to_sequences(review_list)
    padding = pad_sequences(sequence, maxlen=MAXLEN, padding='post', truncating='post')
    return padding