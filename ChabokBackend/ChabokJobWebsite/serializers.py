from rest_framework import serializers


class loginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=128, allow_blank=False)
    password = serializers.CharField(max_length=128)
    