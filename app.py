from flask import Flask, app,jsonify;
app = Flask(__name__)

@app.route('/index')
def index():
    return '<h1> SSL certificado </h1>'

if __name__ == '__main__':
    app.run()