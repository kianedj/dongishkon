from rest_framework import serializers
from .models import DongishGroup, Transaction
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer


class DongishGroupSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source='creator.username')
    members = serializers.SlugRelatedField(
                            queryset=get_user_model().objects.all(),
                            many=True,
                            slug_field="username")
    class Meta:
        model = DongishGroup
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')
    class Meta:
        model = Transaction
        fields = '__all__'

