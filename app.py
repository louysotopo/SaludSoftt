from flask import Flask, app,jsonify,request;
from flask_cors import CORS;
from flask_mail import Mail, Message 
import joblib
import numpy as np
from flask import Flask,request
from flask import jsonify
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
        message = ""
        try:
            model = joblib.load('best_model.pkl')
            x_test = np.array([  data["age"], data["gender"], data["polyura"], data["polydipsia"],
            data["weigtht_loss"],data["weakness"],data["polyfagia"],data["genital_thrush"],
            data["visual_blurring"],data["itchinf"],data["irritabilty"],data["delayed_healing"],
            data["partial_paresis"],data["muscle_stiffness"],data["Alopecia"],data["Obesity"]])
            prediction = model.predict(x_test.reshape(1,-1))
            if str(prediction) == "[1]":
                message = "Con diabetes"        
            else:
                message = "Sin diabetes"        
        except Exception as e: 
                message = e.message
            
    return jsonify({'prediccion': message})        
    
if __name__ == '__main__':
    
    app.run(port=8200)