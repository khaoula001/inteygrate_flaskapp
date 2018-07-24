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
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
logging.warning('------> CHAKIB : IN THE SCRIPT..... !')

@app.route('/', methods = ['GET'])
def hello_world():
    logging.warning('------> CHAKIB : hello_world !')
    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    logging.warning('------> CHAKIB : msg !')
    to = request.form['to']
    return str(to)

@app.route('/sendmsg', methods = ['GET'])
def sendmsg():
    logging.warning('------> CHAKIB : sendmsg !')
    to = request.args.get('to')
    msg = request.args.get('msg')
    token = request.args.get('token')
    if(str(token) == expected_token):
        logging.warning('------> CHAKIB : Before new Client !')
        client = Client(login='212679077037', password='xqbPaGV2DVGB80gdPiDiSZg7biU=')
        logging.warning('------> CHAKIB : after new Client !')
        logging.warning('------> CHAKIB : before send message !')
        res = client.send_message(to, msg)  
        logging.warning('------> CHAKIB : after send message !')
    else:
        res = 'Unauthorized'
    
    logging.warning('------> CHAKIB : finish !')
    return str(res)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
