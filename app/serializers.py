from rest_framework import serializers
from .models import Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('FirstName', 'LastName', 'Email','Phone','Password')
        extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = Student.objects.create(**validated_data)
        return user