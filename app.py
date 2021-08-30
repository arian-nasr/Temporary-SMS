from flask import Flask, jsonify, request
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import sqlconnector as sql
from datetime import datetime

# configuration
DEBUG = True
client = Client('ACdc4061aaeb33b9e5ae6f1caa187114c1','f801f6c98191da45375abfc1c41e2238')

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message', methods=['POST'])
def inbound_sms():
    response = MessagingResponse()
    message_sender = request.form['From']
    message_body = request.form['Body']
    message_date = datetime.now()
    sql.write_to_database('phone1', message_date, message_sender, message_body)
    return str(response)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# sanity check route
@app.route('/auth1', methods=['GET'])
def auth1():
    if sql.is_in_use('authentication', '0e443fd'):
        return jsonify('true')
    else:
        return jsonify('false')

@app.route('/available', methods=['GET'])
def available():
    numbers = sql.read_availability_from_database('numbers')
    return jsonify({
        'status': 'success',
        'numbers': numbers
    })


@app.route('/messages', methods=['GET'])
def allmessages():
    messages = sql.read_messages_from_database('phone1')
    return jsonify({
        'status': 'success',
        'messages': messages
    })


if __name__ == '__main__':
    app.run(host="192.168.0.21")