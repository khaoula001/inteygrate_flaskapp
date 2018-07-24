from flask import Flask
from flask import request

#WA[
from whatsapp import Client
expected_token = 'mySecretToken'
#]WA

app = Flask(__name__)



@app.route('/')
def hello_world():
    logging.warning('------> CHAKIB : hello_world !')
    return 'Hello World!'

@app.route('/msg', methods = ['POST'])
def msg():
    logging.warning('------> CHAKIB : msg !')
    to = request.form['to']
    return str(to)

@app.route('/sendmsg')
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
    app.run()
