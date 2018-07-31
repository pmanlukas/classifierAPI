# classifierAPI
A simple Flask web service to implement an API for a keras classifier based on the following [tutorial](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html) and my own custom classifier for openAPI specifications. 

The API accepts a POST request with a JSON encoded [openAPI Spec](https://github.com/OAI/OpenAPI-Specification) as payload. The response is the predicted category of the API based on the classifier implemented in the API. The API only accepts the Version 2.0 of the [OAS](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) as input and only one file per request. 

The API can either be run through the Python script "classifier_api.py" or as a docker container that is either build with the dockerfile or by using the image from my [dockerhub repo](https://hub.docker.com/r/lukaspman/). To run the Python script either the Anaconda Enviroment (enviroment.yml file) or the PIP requirements file must be installed.

This simple implementation is created only as a proof of concept to demonstrate the ability to use the created classifier from my master thesis in a application scenario. It is not production ready and also the docker images are not maintained or hardened. 

The "api_consumer.py" Python script creates a sample API call with a sample OAS JSON file. 

## Instructions to run the predictive web service

#### as Python script:

You need to have Python 3.6 installed!

First clone the repo "classifierAPI" onto your machine and cd into the main directory.

The following steps are necessesary to install all required Python dependencies:

1. cd to the directory where requirements.txt is located.
2. activate your virtualenv.
3. run: `pip install -r requirements.txt in your shell.`

Then start the api on your machine with the following command in your Python terminal/bash:
`python classifier_api.python`

You can then use the test request with Curl or your browser to see if the api is running. 

In your browser enter the following url:
`http://localhost:5000/`
The response should be:
`Hello World!`

With curl enter the following curl statement:
`curl http://localhost:5000/`
The response should be:
`<h1>Hello World!</h1>`

#### as Docker container:

You can build the docker container yourself with the provided Dockerfile by using the following commands:
`docker build --rm -f Dockerfile -t classifierapi:latest .`
and then run the container with the following command:
`docker run -p 5000:5000 -it consumerapi`

You can also use the image from dockerhub to run the container:
``

#### sample request with CURL:
`curl -X POST -F data=@test.json 'http://127.0.0.1:5000/predict'`

#### sample request with api_consumer Python script:

You need to have Python 3.6 installed!

First clone the repo "classifierAPI" onto your machine and cd into the main directory.

The following steps are necessesary to install all required Python dependencies:

1. cd to the directory where requirements.txt is located.
2. activate your virtualenv.
3. run: `pip install -r requirements.txt in your shell.`

Then start the test script on your machine with the following command in your Python terminal/bash:
`python api_consumer.py`
