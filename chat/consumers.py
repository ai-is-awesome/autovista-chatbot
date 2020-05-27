import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response_message = 'Hello, How can I help you?'
        message_parts = message.split()

        response_message = 'You\'ve entered %s' % (message)

        self.send(text_data=json.dumps({
            'message': response_message,
            'type': 'chat_message'
        }))



