from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('calories_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = 1 if request.form['gender'] == 'male' else 0
    age = float(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    duration = float(request.form['duration'])
    heart_rate = float(request.form['heart_rate'])
    body_temp = float(request.form['body_temp'])

    features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)[0]
    prediction = round(prediction, 2)

    return render_template('index.html', result=prediction)

if __name__ == '__main__':
    app.run(debug=True)
