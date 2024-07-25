import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def marks_prediction(hrs):
    x = pd.read_csv("Linear_X_Train (1).csv")
    y = pd.read_csv("Linear_Y_Train (1).csv")

    x = x.values.astype(float).reshape(-1, 1)
    y = y.values.ravel().astype(float)

    reg = LinearRegression()
    reg.fit(x, y)

    x_test = np.array(hrs).reshape(-1, 1)
    return reg.predict(x_test)[0]
