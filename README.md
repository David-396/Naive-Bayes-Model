Naive Bayes Classifier Server
A FastAPI-based system that enables classification of records using a Naive Bayes model. The system is composed of two servers:

Classifier Server – responsible for receiving classification requests.

Server Side – responsible for preparing data, training the model, evaluating it, and sending it to the classifier when needed.

🚀 General Structure
Naive_Bayes/
│
├── classifier_server/  # Classification request server
│   ├── classifier.py
│   ├── classifier_route.py  # The /classify-record endpoint
│   ├── requirements.txt
│   └── Dockerfile
│
├── server_side/  # Model training server
│   ├── data/
│   ├── data_handling/  # Loading and cleaning
│   │   ├── data_cleaning.py
│   │   └── data_loader.py
│   ├── model/  # Naive Bayes model and accuracy tests
│   │   ├── naive_bayes_model.py
│   │   └── test_accuracy.py
│   ├── server_statics/
│   ├── run_server.py
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── test_server.py
└── start.sh


🧠 How It Works
Step 1: Classification Request
The client sends a POST request to the endpoint: record-classify/
with a JSON body containing a list of values to classify.

Step 2: Check for Existing Model
If a trained model already exists, the server uses it and returns the classification (the value with the highest probability).

If no model exists, the server makes a GET request to the external training server.

Step 3: Model Training (on the Server Side)
The second server (Server Side) loads the data (data_loader.py).

Cleans it (data_cleaning.py).

Trains a Naive Bayes model (naive_bayes_model.py).

Tests the model’s performance (test_accuracy.py).

Returns the model as a dictionary with probabilities for each possible value.

Step 4: Final Classification
The Classifier receives the model, classifies the incoming record, and returns the predicted label.

🧪 Testing
The file test_server.py allows testing the classification functionality.

The code also includes accuracy tests for the trained model.

🐳 Docker
Each server has its own Dockerfile and can be run in separate containers. For quick deployment:
./start.sh

📬 Example of a POST Request
POST /classify-record
Content-Type: application/json
{
  "record": [1.2, 3.4, 5.6, 7.8, 0.9]
}
