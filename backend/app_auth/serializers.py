from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])

        if not user:
            raise serializers.ValidationError("Incorrect username or password.")

        if not user.is_active:
            raise serializers.ValidationError("User is disabled.")

        return {"user": user}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {
            "password": {"required": True, "write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data.pop("username"),
            password=validated_data.pop("password"),
            email=validated_data.pop("email"),
            **validated_data
        )
