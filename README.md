Marks Prediction

A simple machine learning project that predicts student marks based on the number of study hours using Linear Regression. This project includes a web interface built with Flask.

## Features

- Predict marks based on study hours
- Trained using Linear Regression
- Simple and clean web interface using Flask

## Project Structure

Marks_Prediction/
├── app.py #Main Flask application
├── marks.py # Model training and prediction logic
├── home/
│ ├── index.html # Home page template
│ └── sub.html # Result display template
├── Linear_X_Train (1).csv # Study hours dataset
└── Linear_Y_Train (1).csv # Marks dataset

bash
Copy
Edit

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/sathishkumar-08/Marks_Prediction.git
cd Marks_Prediction

(Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
Install the required libraries:

pip install -r requirements.txt
If there's no requirements.txt, install manually:

pip install flask pandas scikit-learn
## Run the app:
python app.py
## Open your browser and go to:
http://127.0.0.1:5000/
## Dataset
Linear_X_Train (1).csv: Contains study hours
Linear_Y_Train (1).csv: Contains corresponding marks

## Model
Algorithm: Linear Regression
Input: Study Hours
Output: Predicted Marks

Contact
Created by Sathish Kumar


