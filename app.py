import sys
import os
import logging
from flask import Flask
from flask import request

logger = logging.getLogger(__name__)
logger.info('some important infos')


#WA[
from whatsapp import Client
expected_token = 'mySecretToken'
#]WA

app = Flask(__name__)

logger.info('------> CHAKIB : IN THE SCRIPT..... !')

@app.route('/', methods = ['GET'])
def hello_world():
    logger.info('------> CHAKIB : hello_world !')
    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    logger.info('------> CHAKIB : msg !')
    to = request.form['to']
    return str(to)

@app.route('/sendmsg', methods = ['GET'])
def sendmsg():
    logger.info('------> CHAKIB : sendmsg !')
    to = request.args.get('to')
    msg = request.args.get('msg')
    token = request.args.get('token')
    if(str(token) == expected_token):
        logger.info('------> CHAKIB : Before new Client !')
        client = Client(login='212679077037', password='xqbPaGV2DVGB80gdPiDiSZg7biU=')
        logger.info('------> CHAKIB : after new Client !')
        logger.info('------> CHAKIB : before send message !')
        res = client.send_message(to, msg)  
        logger.info('------> CHAKIB : after send message !')
    else:
        res = 'Unauthorized'
    
    logger.info('------> CHAKIB : finish !')
    return str(res)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
