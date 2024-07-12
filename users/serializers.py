from rest_framework import serializers
from users.models import User
import re
from django.core.validators import validate_email
from django.utils.translation import gettext as trans

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','firstname', 'lastname', 'email', 'phone_number')
        extra_kwargs = {
            'password': {'write_only': False}
        }

    def validate_phone_number(self, value):
        regex = r"^\d{10}$"

        if not re.match(regex, value):
            raise serializers.ValidationError(trans('valid_phone_number_format'))

        return value
        
    def validate_email(self, value):
        if validate_email(value):
            raise serializers.ValidationError(trans('valid_email_format'))

        return value
     