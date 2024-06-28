from django.db import models
from django.utils import timezone

from ..Saas.models import AppUser, rand_str



# Create your models here.
class Conversation(models.Model):
    sn = models.CharField(default=rand_str, max_length=20, unique=True)
    user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True, related_name="conversations")
    share = models.BooleanField(default=False)
    started = models.DateField(default=timezone.now)
    modified = models.DateField(default=timezone.now)

    def is_shared(self):
        return self.share
    
    def clone(self):
        return self.messages.all()
        pass


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()
    file = models.URLField(null=True)
    user_sent = models.BooleanField()