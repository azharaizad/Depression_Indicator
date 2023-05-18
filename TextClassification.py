import streamlit as st
from hashlib import new
from imp import new_module
from pyexpat import model
from re import sub
from unittest import result
import requests
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import numpy as np
import time
import pickle

class TextClassificationPage:
    def __init__(self):
        pass

    def render(self):
        st.title("Text Classification Page")
        st.write("This is the text classification page.")
        def load_model():
            new_model = tf.keras.models.load_model('C:\\Users\\aizad\\OneDrive\\Desktop\\Depression_Indicator\\model_depressed_2.h5')
            return new_model

        def sentence_process(sentence):
            max_length = 120
            with open('C:\\Users\\aizad\\OneDrive\\Desktop\\Depression_Indicator\\tokenizer.pickle', 'rb') as handle:
                tokenizer = pickle.load(handle) 
            new_sentences = tokenizer.texts_to_sequences(sentence)
            new_padded = pad_sequences(new_sentences, maxlen=max_length)
            return new_padded

        with st.spinner("Loading Model. . . ."):
            new_model = load_model() 
        
        with st.form(key = 'form_1'):
            input_1 = st.text_area(label = 'Please enter one sentence to represent your feelings', height=100)
            confirm_button = st.form_submit_button(label= 'Confirm')
            arr = np.array([input_1])
            padded_sentence = sentence_process(arr)
            results = new_model.predict(padded_sentence)
            if results[0,0] > 0.75:
                results_2 = "Severe depression"
                advice = "Counseling for depression: Since your depression symptoms are very serious, please seek for the help of a professional counsellor. So, you will explore why depression has occurred and look for ways to overcome it."
                st.error("Severe depression detected")
            elif 0.5 <= results[0,0] <= 0.75:
                results_2 = "Moderate depression"
                advice = "Talking therapy: Please have a try on talking therapy to destress yourself. Talking therapy is a series of sessions, the individual will work with a counselor to identify the causes of depression and find ways of resolving it."
                st.warning("Moderate depression detected")
            elif 0.25 <= results[0,0] <= 0.5:
                results_2 = "Mild depression"
                advice = "Guided self-help: Since your depression symptoms are not too serious, you may follow an online course or manual with the support of a therapist. The course aims to provide tools that enable a person to make helpful changes."
                st.info("Mild depression detected")
            elif 0.001 <= results[0,0] <= 0.25:
                results_2 = "No depression"
                advice = "you are totally fine"
                st.success("No depression detected")
            else:
                results_2 =""
                advice = ""
            
        st.markdown("## Prediction Result")
        st.markdown(f"Predictions : {results_2}")
        my_bar = st.progress(0)

        for percent_complete in range(int(results[0,0] * 100)):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)

        resultPercentage = "{:.2f}".format(results[0,0] * 100)
        st.markdown(f"The Probability of being depressed : {resultPercentage} %")
        st.markdown("## Advice for " + f"{results_2}")
        st.info(advice)

# Instantiate the TextClassificationPage class
TextClassification = TextClassificationPage()

