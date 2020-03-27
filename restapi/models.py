from django.db import models
from apps.models import Account
from datetime import datetime
import jsonfield

# Create your models here.

class SwitchJson(models.Model):
    user=models.OneToOneField(Account , on_delete=models.CASCADE , null=True)
    switch = jsonfield.JSONField()
    switch_name = jsonfield.JSONField()
    

    def __str__(self):
        try:
            return self.user.username
        except:
            return str(self.id)