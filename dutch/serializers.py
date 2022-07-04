from dataclasses import fields
from rest_framework import serializers
from .models import DongishGroup, Transaction

class DongishGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DongishGroup
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

