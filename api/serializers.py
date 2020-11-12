from rest_framework import serializers
from authentication.models import User



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['id',
        'first_name',
        'last_name',
        'fullname',
        'username',
        'email',
        'password',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }