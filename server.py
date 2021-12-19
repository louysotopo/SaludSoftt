import joblib
import numpy as np
import pandas as pd
import sklearn

from flask import Flask, render_template, request
from flask import jsonify

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import (
    cross_val_score, KFold
)


import matplotlib.pyplot as plt 


from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA
 
from sklearn.linear_model import LogisticRegression
 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

app = Flask(__name__)

#POSTMAN PARA PRUEBAS
@app.route('/predict/', methods=['GET','POST'])
def predict():
    x_test = np.array([[61,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0],
            [60,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [58,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0],
            [54,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [67,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0],
            [66,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0],
            [43,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [62,0,1,1,1,1,0,0,1,0,0,0,1,0,0,1],
            [54,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0],
            [39,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0],
            [48,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0],
            [58,0,1,1,1,1,1,0,1,0,0,0,1,1,0,1],
            [32,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0],
            [42,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    prediction = model.predict(x_test.reshape(14,-1))
    return jsonify({'prediccion': str(prediction)})
        


if __name__ == "__main__":
    model = joblib.load('./models/best_model.pkl')
    app.run(port=8200)
    