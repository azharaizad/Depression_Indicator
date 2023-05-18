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
from keras_preprocessing.sequences import pad_sequences

import numpy as np
import time
import pickle

def TextClassification():
    st.title("Text Classification")
    st.write("Welcome to Text Classification!")

if __name__ == "__main__":
    TextClassification()

def load_model():
    new_model = tf.keras.models.load_model('model_depressed_2.h5')
    return new_model

with open('tokenizer.pickle','rb') as handle:
    tokenizer = pickle.load(handle)

def sentence_process(sentence):
    max_length = 200
    new_sentences = tokenizer.texts_to_sequences(sentence)
    new_padded = pad_sequences(new_sentences, maxlen = max_length)
    return new_padded
    

