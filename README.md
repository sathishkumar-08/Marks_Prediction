Overview
This project employs a simple linear regression model to forecast student scores based on the number of hours studied. The model is trained on a dataset containing study hours and corresponding marks. A Flask web interface allows users to input study hours and receive predicted marks.

🚀 Features
Linear regression model for prediction
User-friendly Flask web interface
Input form for study hours
Real-time prediction display

📁 Project Structure
Marks_Prediction/
├── app.py
├── marks.py
├── home/
│   ├── index.html
│   └── sub.html
├── Linear_X_Train (1).csv
└── Linear_Y_Train (1).csv
app.py: Main Flask application
marks.py: Model training and prediction logic
home/index.html: Homepage template
home/sub.html: Result display template
Linear_X_Train (1).csv: Dataset of study hours
Linear_Y_Train (1).csv: Dataset of corresponding marks

🛠️ Setup Instructions
Clone the repository:
git clone https://github.com/sathishkumar-08/Marks_Prediction.git
cd Marks_Prediction
Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required packages:
pip install -r requirements.txt
Note: If requirements.txt is not present, install packages manually:
pip install flask pandas scikit-learn

Run the application:
python app.py
Access the application:
Open your browser and navigate to http://127.0.0.1:5000/

📊 Dataset
The dataset comprises two CSV files:
Linear_X_Train (1).csv: Contains the number of study hours.
Linear_Y_Train (1).csv: Contains the corresponding marks.
These datasets are used to train the linear regression model.

📈 Model Details
Algorithm: Linear Regression
Input Feature: Study Hours
Output: Predicted Marks
The model is trained using scikit-learn's LinearRegression class.

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
For any inquiries or feedback, please contact sathishkumar-08.
