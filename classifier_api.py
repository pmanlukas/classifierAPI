import numpy as np
import pandas as pd
import json
import pickle
import sklearn
import flask
import io
from collections import Counter
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib
from sklearn import preprocessing


# initialize our Flask application and the classifier model
app = flask.Flask(__name__)

model = None

# this method loads the pretrained transformer


def load_tftransformer():
    with open(r"C:\Users\lukas\Desktop\classifierAPI\obj\tf_transformer.pickle", 'rb') as handle:
        tf_transformer = pickle.load(handle)
    return tf_transformer

# this method loads the pretrained model and its weights


def load_models():
    # load model with its weights
    print("loading model and weights...")
    global model

    model = joblib.load(
        r"C:\Users\lukas\Desktop\classifierAPI\obj\model_svm_C.pickle")
    print("loaded model")

    print("loading tokenizer ...")
    global tf_transformer
    tf_transformer = load_tftransformer()
    print("loaded tokenizer")


# this function is preprocessing the data
def preprocess_data(spec):
    # turn json into string
    processed_spec = []
    info = spec['info']
    strSpec = str(info)
    processed_spec.append(strSpec)

    # tokenzie spec and generate a vector representation
    data = tf_transformer.transform(processed_spec)
    return data

# this model loads the label encoder


def load_encoder():
    with open(r"C:\Users\lukas\Desktop\classifierAPI\obj\encoder.pickle", 'rb') as handle:
        encoder = pickle.load(handle)
    return encoder

# this function adds the endpoint for our api


@app.route("/predict", methods=["POST"])
def predict():
    # preparation of response object
    data = {"success": False}

    # checks for post request
    if flask.request.method == "POST":

        # read the spec in json
        spec = flask.request.get_json()

        # preprocess the specification and prepare it for classification
        spec = preprocess_data(spec)

        # classify the input spec and then initialize the dict
        # of predictions to return to the client
        print(spec)
        print(spec.shape)
        prediction = model.predict(spec)

        # transform prediction into its label
        encoder = load_encoder()
        label = encoder.inverse_transform(prediction)

        # add label to response
        data["predictions"] = str(label)

        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    response = json.dumps(data)
    return response


if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."))
    load_models()
    app.run()
