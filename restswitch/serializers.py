from rest_framework import serializers
from .models import Switch


class SwitchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Switch
        fields = ['id', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 'd1', 'd2', 'd3', 'd4', 'd5', ]
        allow_null_fields=['id', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 'd1', 'd2', 'd3', 'd4', 'd5', ]