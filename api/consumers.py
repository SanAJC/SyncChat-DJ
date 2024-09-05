import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Chat, Message 
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from channels.exceptions import DenyConnection


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        #self.room_group_name = 'test'
       
        token = self.scope['query_string'].decode().split('=')[1]

        try:
            UntypedToken(token)
            # Obtener el nombre de la sala desde la URL
            self.room_group_name = self.scope["url_route"]["kwargs"]["room_name"]
            #self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
            #self.room_group_name = "chat_%s" % self.room_name

            # Verifica la existencia de la sala
            try:
                Chat.objects.get(name=self.room_group_name)
            except Chat.DoesNotExist:
                print(f'Chat room {self.room_group_name} does not exist')
                self.close()
                return

            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()

        except (InvalidToken, TokenError):
            self.close()

    def receive(self,text_data):
        text_data_json=json.loads(text_data)
        message = text_data_json['message']
        user_id = self.scope['user'].id  

        # Guardar el mensaje en la base de datos
        chat = Chat.objects.get(name=self.room_group_name)  
        user = User.objects.get(id=user_id)
        Message.objects.create(chat=chat, user=user, content=message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username': user.username 
            }
            
        )
    
    def chat_message(self,event):
        message=event['message']
        username = event['username'] 

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username': username
        }))