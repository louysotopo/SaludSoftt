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
            x_test = np.array([  data["age"], data["gender"], int(data["polyura"]), int(data["polydipsia"]),
            int(data["weigtht_loss"]),int(data["weakness"]),int(data["polyfagia"]),int(data["genital_thrush"]),
            int(data["visual_blurring"]),int(data["itchinf"]),int(data["irritabilty"]),int(data["delayed_healing"]),
            int(data["partial_paresis"]),int(data["muscle_stiffness"]),int(data["Alopecia"]),int(data["Obesity"])])
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