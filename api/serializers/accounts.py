from rest_framework import serializers
from accounts.models import User
from profiles.models import Profile
import phonenumbers
from django.contrib.auth import password_validation

def field_length(fieldname):
    field = next(field for field in User._meta.fields if field.name == fieldname)
    return field.max_length

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar','bio')

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()

    def get_avatar(self, user):
        try:
            return user.profile.avatar.url
        except:
            return ''

    def get_bio(self, user):
        try:
            return user.profile.bio
        except:
            return ''

    class Meta:
        model = User
        fields = ('username', 'email', 'fullname', 'is_verified', 'card_id',
                  'phone_number', 'contact', 'institution', 'avatar', 'bio')


class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=field_length('password'), required=True)
    email = serializers.EmailField(max_length=field_length('email'), required=True)
    fullname = serializers.CharField(max_length=field_length('fullname'), required=True)
    username = serializers.CharField(max_length=field_length('username'), required=True)
    phone_number = serializers.CharField(max_length=15, required=True)

    def validate_password(self, value):
        password_validation.validate_password(password=value, user=User)
        return value

    def validate_email(self, value):
        value = value.lower()

        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('A user with that email address already exists')
        return value

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('A user with that username already exists')
        return value

    def validate_phone_number(self, value):
        phone_number = phonenumbers.parse(value, "ID")

        if phonenumbers.is_valid_number(phone_number):
            return phonenumbers.format_number(
                phone_number, phonenumbers.PhoneNumberFormat.E164
            )
        else:
            raise serializers.ValidationError('Phone number is not valid.')

    def create(self, validated_data):
        return User.objects.create(username=validated_data['username'],
                                   email=validated_data['email'],
                                   password=validated_data['password'],
                                   fullname=validated_data['fullname'],
                                   phone_number=validated_data['phone_number'])
