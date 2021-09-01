from flask import Flask, jsonify, request
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import sqlconnector as sql
from datetime import datetime
import os

# configuration
DEBUG = True
twilio_sid = os.environ.get('TWILIO_SID')
twilio_secret = os.environ.get('TWILIO_SECRET')
client = Client(twilio_sid, twilio_secret)

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/api/temporarysms/writemessage', methods=['POST'])
def inbound_sms():
    response = MessagingResponse()
    message_sender = request.form['From']
    message_body = request.form['Body']
    message_date = datetime.now()
    sql.write_to_database('phone1', message_date, message_sender, message_body)
    return str(response)

@app.route('/api/temporarysms/available', methods=['GET'])
def available():
    numbers = sql.read_availability_from_database('numbers')
    return jsonify({
        'status': 'success',
        'numbers': numbers
    })

@app.route('/api/temporarysms/readmessage', methods=['GET'])
def allmessages():
    messages = sql.read_messages_from_database('phone1')
    return jsonify({
        'status': 'success',
        'messages': messages
    })

if __name__ == '__main__':
    app.run(host="192.168.0.21")