#import library
import uvicorn
from fastapi import FastAPI
from IrisiModel import Iris
import pickle


# create the app object
app = FastAPI()
pickle_model = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_model)

# default route


@app.get('/')
def index():
    return{"message": "Hello IDM Students"}

# default route


@app.get('/api-demo')
def index():
    return{"message": "This is demo API"}

# Prediction Function, return the predicted result in JSON


@app.post('/predict')
def predict(data: Iris):
    # convert data obj to dictionary
    data = dict(data)
    sepalLength = data['sepal_length']
    petalLength = data['petal_length']
    sepalWidth = data['sepal_width']
    petalWidth = data['petal_width']
    # prediction
    prediction = classifier.predict(
        [[sepalLength, petalLength, sepalWidth, petalWidth]])

    return {
        'prediction': prediction[0]
    }


# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


# Command to run API server
# python -m uvicorn main:app --reload
