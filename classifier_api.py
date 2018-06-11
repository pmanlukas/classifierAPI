#TODO: Add imports for keras
import numpy as np
import json
import flask
import io

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None

#this method loads the pretrained model and its weights
def load_model():
    #TODO: add code to load model and word embeddings
    
    #add creation of embedding layer here
    
    global model
    #add loading of model and weights here

#this function is preprocessing the data
def preprocess_data(spec):
    processed_spec = []
    strSpec = json.dumps(spec)
    processed_spec.append(strSpec)
   
    return processed_spec