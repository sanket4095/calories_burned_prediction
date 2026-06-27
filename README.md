# Calories Burned Prediction

A simple ML project that predicts how many calories you burn during 
exercise, based on things like duration, heart rate and body temperature.

## What it does

I trained a Linear Regression model on a Kaggle dataset of 15,000 
exercise sessions. The model takes your age, gender, height, weight, 
exercise duration, heart rate and body temperature, and predicts 
calories burned.

## Results

- R² score: 0.967
- RMSE: 11.49

## Things I found while building this

- Duration, heart rate and body temp are highly correlated with each 
  other since they all increase together during exercise. This caused 
  weird coefficient signs for body temp even though the model still 
  worked well overall.
- The model gives unrealistic results if you enter exercise duration 
  above 30 minutes, since the training data only goes up to 30 mins. 
  Linear regression just extends the line, which doesn't make sense 
  in real life.

## How to run it

pip install -r requirements.txt

python app.py

Then open localhost:5000 in your browser.

##  Skills Demonstrated

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `Scikit-learn` · `Linear Regression` · `Feature Engineering` · `Cross Validation` · `Flask` · `Model Deployment`

---

##  Author

**Sanket** — B.Tech CSE, NIT Goa
