from rest_framework import serializers
from pybo.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['account', 'passwd', 'nickname', 'email', 'mobile']