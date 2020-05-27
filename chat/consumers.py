import json
from channels.generic.websocket import WebsocketConsumer


commands = {
    'name' : 'Hi, Please enter your name. ',
    'help' : 'How can I help you?', 
    'contact' : 'Please enter your contact information'

}







class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass



    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        if message in commands:
            if message == 'name':
                response_message = 'Hi, %s. Nice to meet you. ' %(message)

            if message == 'help':
                response_message = 'How can I help you?'

            if message == 'contact':
                response_message = 'Please enter your contact information. '



        else:
            response_message = 'Invalid response, please choose from either name, help or contact'

        message_parts = message.split()


        

        self.send(text_data=json.dumps({
            'message': response_message,
            'type': 'chat_message'
        }))




