import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from .models import Chat, Message

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        #self.room_group_name = 'test'
        # Obtener el nombre de la sala desde la URL
        self.room_group_name = f'chat_{self.scope["url_route"]["kwargs"]["room_name"]}'

        try:
            self.chat = Chat.objects.get(name=self.room_group_name)
        except Chat.DoesNotExist:
            # Si el chat no existe, cerrar la conexión
            self.close()
            return
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self,text_data):
        text_data_json=json.loads(text_data)
        message = text_data_json['message']
        user_id = self.scope['user'].id  # Obtener el ID del usuario actual

        # Guardar el mensaje en la base de datos
        chat = Chat.objects.get(name=self.room_group_name)  # Obtener el chat correspondiente
        user = User.objects.get(id=user_id)
        Message.objects.create(chat=chat, user=user, content=message)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
            
        )
    
    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))