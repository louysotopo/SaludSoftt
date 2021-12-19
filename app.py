from flask import Flask, app,jsonify,request;
from flask_cors import CORS;
from flask_mail import Mail, Message 


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
CORS(app)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'louysotopo123@gmail.com',
    MAIL_PASSWORD = 'rfxxnalvdpdylkth'
)
mail = Mail(app) 

@app.route('/correo/send/',methods = ['POST','GET'])
def sendEmail():
    data = request.json
    if request.method == 'POST':
        try:
            dest=data["destinatario"].split(sep=';')
            msg = Message(data["asunto"], sender=app.config['MAIL_USERNAME'], recipients=dest)
            msg.body = data["mensaje"]
            mail.send(msg)
            return jsonify({"resultado":"Enviado"})
        except Exception as e:
            return jsonify({"resultado":e})
    if request.method == 'GET':
        try:
            dest=data["destinatario"].split(sep=';')
            msg = Message(data["asunto"], sender=app.config['MAIL_USERNAME'], recipients=dest)
            msg.body = data["mensaje"]
            mail.send(msg)
            return jsonify({"resultado":"Enviado"})
        except Exception as e:
            return jsonify({"resultado":e})

@app.route('/predict/',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        data = request.json
        x_test = np.array([  data["age"], data["gender"], int(data["polyura"]), int(data["polydipsia"]),
        int(data["weigtht_loss"]),int(data["weakness"]),int(data["polyfagia"]),int(data["genital_thrush"]),
        int(data["visual_blurring"]),int(data["itchinf"]),int(data["irritabilty"]),int(data["delayed_healing"]),
        int(data["partial_paresis"]),int(data["muscle_stiffness"]),int(data["Alopecia"]),int(data["Obesity"])])
        prediction = model.predict(x_test.reshape(1,-1))
        if str(prediction) == "[1]":
            return jsonify({'prediccion': "Con Diabetes"})        
        else:
            return jsonify({'prediccion': "Sin Diabetes"})        
    
if __name__ == '__main__':
    model = joblib.load('./models/best_model.pkl')
    app.run(port=8200)