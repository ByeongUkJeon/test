from rest_framework import serializers
from pybo.models import User, Tale


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['account', 'passwd', 'nickname', 'email', 'mobile']


class TaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tale
        fields = ['num', 'imglink', 'title', 'content']
