# TODO: Add code to create openAPI spec of this api
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

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)

model = None
#filepath_model = r'C:\Users\lukas\Desktop\classifierAPI\obj\CNN_cat.h5'  # TODO: add filepath of model


# this method loads the pretrained model and its weights
def load_tftransformer():
    with open(r"C:\Users\lukas\Desktop\classifierAPI\obj\tf_transformer.pickle", 'rb') as handle:
        tf_transformer = pickle.load(handle)
    return tf_transformer


def load_models():
    # load model with its weights
    print("loading model and weights...")
    global model
    #model = load_model(r"C:\Users\lukas\Desktop\classifierAPI\obj\model_svm_C.pickle")
    model = joblib.load(r"C:\Users\lukas\Desktop\classifierAPI\obj\model_svm_C.pickle")
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


# this function adds the endpoint for our api
@app.route("/predict", methods=["POST"])
# TODO: add code for swagger file
def predict():
    # preparation of response object
    data = {"success": False}

    # TODO: implement prediction and adjust the code
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        
        # read the spec in json
        spec = flask.request.get_json()

        # preprocess the specification and prepare it for classification
        spec = preprocess_data(spec)

        # classify the input image and then initialize the list
        # of predictions to return to the client
        print(spec)
        print(spec.shape)
        prediction = model.predict(spec)
        
        data["predictions"] = str(prediction)

        # loop over the results and add them to the list of
        # returned predictions

        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    response = json.dumps(data)
    return response
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."))
    load_models()
    app.run()