from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    name = models.CharField(max_length=100)
    is_group = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)

    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}...'

class ChatParticipant(models.Model):
    chat = models.ForeignKey(Chat, related_name='participants', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='chat_participants', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} in {self.chat.name}'









