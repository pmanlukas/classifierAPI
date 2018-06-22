# TODO: Add code to create openAPI spec of this api
import numpy as np
import pandas as pd
import json
import pickle

import flask
from flask_restplus import Resource, Api

import io
from collections import Counter
from datetime import datetime
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import Model
from keras.models import load_model

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)

model = None
filepath_model = 'obj/CNN_cat.h5'  # TODO: add filepath of model


# this method loads the pretrained model and its weights
def load_tokenizer():
    with open('obj/tokenizer_cat.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer


def load_model():
    # load model with its weights
    print("loading model and weights...")
    global model
    model = load_model(filepath_model)
    print("loaded model")

    print("loading tokenizer ...")
    global tokenizer
    tokenizer = load_tokenizer()
    print("loaded tokenizer")


# this function is preprocessing the data
def preprocess_data(spec):
    # turn json into string
    processed_spec = []
    strSpec = json.dumps(spec)
    processed_spec.append(strSpec)

    # tokenzie spec and generate a vector representation
    sequences = tokenizer.texts_to_sequences(processed_spec[0])

    word_index = tokenizer.word_index
    print('Found %s unique tokens.' % len(word_index))

    # pad sequence to have necessary length for final model
    data = pad_sequences(sequences, maxlen=75000)

    return data


# this function adds the endpoint for our api
@app.route("/predict", methods=["POST"])
# TODO: add code for swagger file
def predict():
    # preparation of response object
    data = {"success": False}

    # TODO: implement prediction and adjust the code
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("spec"):
            # read the spec in json
            spec = flask.request.files["specOpenApi"].read()

            # preprocess the specification and prepare it for classification
            spec = preprocess_data(spec)

            # classify the input image and then initialize the list
            # of predictions to return to the client
            y_softmax = model.predict(spec)
            y_pred = []
            probs_list = []
            for i in range(0, len(y_softmax)):
                probs = y_softmax[i]
                probs_list.append(probs)
                predicted_index = np.argmax(probs)
                y_pred.append(predicted_index)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for pred in y_pred:
                r = {"label": pred}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)
