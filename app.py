from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Model load karo
with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    population = int(request.form['population'])
    distance_bus = float(request.form['distance_bus'])
    distance_meerut = float(request.form['distance_meerut'])
    road_paved = int(request.form['road_paved'])

    prediction = model.predict([[population, distance_bus, distance_meerut, road_paved]])

    result = "✅ Direct Transport Milni Chahiye!" if prediction[0] == 1 else "❌ Transport Connectivity Nahi Hai — High Priority Area!"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)