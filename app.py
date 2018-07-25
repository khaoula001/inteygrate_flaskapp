import sys
import os
import logging
from flask import Flask
from flask import request



#WA[
from whatsapp import Client
expected_token = 'mySecretToken'
#]WA

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    to = request.form['to']
    return str(to)

@app.route('/sendmsg', methods = ['GET'])
def sendmsg():
    to = request.args.get('to')
    msg = request.args.get('msg')
    token = request.args.get('token')
    if(str(token) == expected_token):
        client = Client(login='212679077037', password='xqbPaGV2DVGB80gdPiDiSZg7biU=')
        res = client.send_message('212650382336', 'Hi there' ,false)  
    else:
        res = 'Unauthorized'
    
    return str(res)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
