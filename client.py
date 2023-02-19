import requests
from protos.event_pb2 import Event

# Create a new message
message = Event()
message.text = "Hello, world!"

# Send the message to the server
response = requests.post('http://localhost:5000/messages', data=message.SerializeToString())

# Get the ID of the message from the response
message_id = int(response.text)

# Retrieve the message by ID from the server
response = requests.get(f'http://localhost:5000/messages/{message_id}')

# Parse the message from the response
message = Event()
message.ParseFromString(response.content)

# Print the message
print(message.text)
