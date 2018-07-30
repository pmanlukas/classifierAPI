# classifierAPI
A simple Flask web service to implement an API for a keras classifier based on the following [tutorial](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html) and my own custom classifier for openAPI specifications. 

The API accepts a POST request with a JSON encoded [openAPI Spec]() as payload. The response is the predicted category of the API based on the classifier implemented in the API. The API only accepts the Version 2.0 of the [OAS]() as input and only one file per request. 

The API can either be run through the Python script "classifier_api.py" or as a docker container that is either build with the dockerfile or by using the image from my [dockerhub repo](). To run the Python script either the Anaconda Enviroment (enviroment.yml file) or the PIP requirements file must be installed.

This simple implementation is created only as a proof of concept to demonstrate the ability to use the created classifier from my master thesis in a application scenario. It is not production ready and also the docker images are not maintained or hardened. 

## Instructions to run the predictive web service

### as Python script:

### as Docker container:

### sample request with CURL:
`curl -X POST -F data=@test.json 'http://127.0.0.1:5000/predict'`

### sample request with api_consumer Python script:

### sample request with api_consumer Docker container: