"""
from django.db import models
from apps.models import Account
from datetime import datetime
#import jsonfield

# Create your models here.

class Switch(models.Model):
    user=models.OneToOneField(Account , on_delete=models.CASCADE , null=True)
    #data = jsonfield.JSONField()
    s1=models.NullBooleanField(default=None ,null=True)
    s2=models.NullBooleanField(default=None ,null=True)
    s3=models.NullBooleanField(default=None ,null=True)
    s4=models.NullBooleanField(default=None ,null=True)
    s5=models.NullBooleanField(default=None ,null=True)
    s6=models.NullBooleanField(default=None ,null=True)
    s7=models.NullBooleanField(default=None ,null=True)
    s8=models.NullBooleanField(default=None ,null=True)
    s9=models.NullBooleanField(default=None ,null=True)
    s10=models.NullBooleanField(default=None ,null=True)
    d1=models.PositiveSmallIntegerField(default=None ,null=True)
    d2=models.PositiveSmallIntegerField(default=None ,null=True)
    d3=models.PositiveSmallIntegerField(default=None ,null=True)
    d4=models.PositiveSmallIntegerField(default=None ,null=True)
    d5=models.PositiveSmallIntegerField(default=None ,null=True)

    def __str__(self):
        try:
            return self.user.username
        except:
            return str(self.id)
"""