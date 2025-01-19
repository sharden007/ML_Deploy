THis uses:
pandas and scikit-learn to 
build the machine learning model. 
And FastAPI and Uvicorn to build the 
API to serve the model’s predictions.


Incremental learning is particularly useful in 
scenarios where data arrives continuously or is 
too large to fit into memory. This is
 a Python use case for incremental learning using 
 Scikit-Learn's SGDClassifier with the partial_fit 
 method. This approach is ideal for handling streaming 
 data or large datasets.


This code scenario where a financial institution wants
 to predict fraudulent transactions. New transaction 
 data arrives continuously, and the model needs to update 
 incrementally without retraining from scratch.


 Simulating Streaming Data:
The dataset is split into small batches to mimic real-time data streams.
Model Initialization:
SGDClassifier is used with partial_fit, which allows incremental updates.
The classes parameter ensures that the model knows all possible target labels.
Incremental Training:
The partial_fit method updates the model with each new batch of data.
Periodic evaluation helps monitor performance during training.
Final Evaluation:
After training on all batches, the model is evaluated on a separate test dataset.

Build the Docker image by running the following docker build command:

$ docker build -t house-price-prediction-api .
Next run the Docker container:

$ docker run -d -p 80:80 house-price-prediction-api
Your API should now be running and accessible at http://127.0.0.1:80.



To run: in directory: \Repos\ML_Deploy\ML_Deploy

uvicorn app.main:app --reload

You can use curl or Postman to test the /predict endpoint by sending a POST request. Here’s an example request:

In postman:
POST:
  http://127.0.0.1:80/predict
  Body: {
  "MedInc": 3.5,
  "AveRooms": 5.0,
  "AveOccup": 2.0
}'