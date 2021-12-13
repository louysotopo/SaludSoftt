from flask import Flask, app,jsonify,request;
from flask_mail import Mail, Message 

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'caja.pruebasaqp@gmail.com',
    MAIL_PASSWORD = 'Pruebas_CAJA'
)
mail = Mail(app) 

@app.route('/correo/send/')
def sendEmail():
    data = request.json
    try:
        dest=data["destinatario"].split(sep=';')
        msg = Message(data["asunto"],
        sender=app.config['MAIL_USERNAME'],
        recipients=dest)
        msg.body = data["mensaje"]
        mail.send(msg)
        return jsonify({"resultado":"Enviado"})
    except:
         return jsonify({"resultado":"No enviado"})


@app.route('/predict/')
def predict():

    data = request.json

    resultado = ""

    if data["muscle_stiffness"] == True:
        resultado = "Tiene Diabetes"
    else:
        resultado = "No tiene Diabetes"

    return jsonify({"resultado":resultado})

if __name__ == '__main__':
    app.run()