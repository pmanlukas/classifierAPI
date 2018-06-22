# classifierAPI
A simple Flask web service to implement an API for a keras classifier based on the following [tutorial](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html) and my own custom CNN based classifier for openAPI specifications.

## sample request:
`curl -X POST -F spec=@test.json 'http://127.0.0.1:5000/predict'`