# 🚌 Rural Transit Analyzer

## Problem
Many villages in Meerut district have no direct public transport.
People have to walk to a neighboring village first to catch a bus.
I personally come from one such village — this is a real problem I faced.

## Solution
A Machine Learning model that predicts whether a village needs
direct transport connectivity — based on population, distance to
bus stop, distance to Meerut city, and road condition.

## Tech Stack
- Python, Pandas, Matplotlib
- Scikit-learn (Random Forest Classifier)
- Flask (Web Application)

## Project Structure
- `Notebook/analysis.ipynb` — Data analysis and model training
- `Data/villages.csv` — Self-collected village data
- `Model/model.pkl` — Trained ML model
- `app.py` — Flask web application

## Data
20 villages from Meerut district — data self-collected using
local knowledge and Google Maps for distance measurement.

## Model Performance
- Algorithm: Random Forest Classifier
- Accuracy: 100% (Note: Small dataset of 20 villages.
  Real deployment would require district-level census data.)

## What I Would Improve
- Collect more village data (200+ rows)
- Add map visualization
- Use OpenStreetMap API for real distances
- Deploy on cloud (Render/Railway)

## How to Run
pip install flask scikit-learn pandas numpy
python app.py