#TODO: Add code to create openAPI spec of this api
import numpy as np
import pandas as pd
import json
import flask
import io
from collections import Counter
from datetime import datetime
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from keras.models import load_model



# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None
filepath = ""#TODO: add filepath of model


#this method loads the pretrained model and its weights
def load_model():
    #TODO: add code to load model and word embeddings
    model = load_model(filepath)
    #add creation of embedding layer here
    
    global model
    #add loading of model and weights here


#this function is preprocessing the data
def preprocess_data(spec):
    #turn json into string
	processed_spec = []
    strSpec = json.dumps(spec)
    processed_spec.append(strSpec)
   
    #tokenzie spec and generate a vector representation
	tokenizer = Tokenizer(nb_words=35000)
	tokenizer.fit_on_texts(processed_spec[0])
	sequences = tokenizer.texts_to_sequences(processed_spec[0])

	word_index = tokenizer.word_index
	print('Found %s unique tokens.' % len(word_index))

	#pad sequence to have necessary length for final model
	data = pad_sequences(sequences, maxlen=75000)

    return data


#this function adds the endpoint for our api
@app.route("/predict", methods=["POST"])
def predict():
    
    #preparation of response object
    data = {"success": False}
    
    #TODO: implement prediction and adjust the code
    # ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":
		if flask.request.files.get("spec"):
			# read the spec in json
			spec = flask.request.files["specOpenApi"].read()

			# preprocess the specification and prepare it for classification
			spec = preprocess_data(spec)

			# classify the input image and then initialize the list
			# of predictions to return to the client
			preds = model.predict(spec)
			results = imagenet_utils.decode_predictions(preds) # change to own code
			data["predictions"] = []

			# loop over the results and add them to the list of
			# returned predictions
			for (imagenetID, label, prob) in results[0]:
				r = {"label": label, "probability": float(prob)}
				data["predictions"].append(r)

			# indicate that the request was a success
			data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

