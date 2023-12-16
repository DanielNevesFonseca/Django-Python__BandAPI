from django.forms import ValidationError
from django.db import IntegrityError
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'full_name',
            'artistic_name', 'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
            'id': {
                'read_only': True
            },
            'email': {
                'validators': []
            }
        }

    def validate_email(self, email_value):
        if User.objects.filter(email=email_value).exists():
            raise ValidationError("This field must be unique.")
        return email_value

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
