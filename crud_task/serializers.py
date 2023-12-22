# serializers.py
from rest_framework import serializers
from .models import tasktable

class tasktableSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasktable
        fields = '__all__'
