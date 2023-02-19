from flask import Flask, request
from protos.event_pb2 import Event

app = Flask(__name__)

# Store messages in memory
messages = []

@app.route('/messages', methods=['POST'])
def post_message():
    # Parse the message from the request body
    message = Event()
    message.ParseFromString(request.data)

    # Assign a unique ID to the message
    message.id = len(messages) + 1

    # Store the message in memory
    messages.append(message)

    # Return the ID of the message as a response
    return str(message.id)

@app.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    # Find the message by ID
    for message in messages:
        if message.id == message_id:
            # Serialize the message to a byte string and return it as a response
            return message.SerializeToString()

    # Return a 404 error if the message was not found
    return '', 404

app.run()
