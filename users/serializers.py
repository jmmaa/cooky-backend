from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:  # pyright: ignore [reportIncompatibleVariableOverride]
        model = User
        fields = "__all__"
