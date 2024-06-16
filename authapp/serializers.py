from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import NewUser

class CustomRegisterSerializer(RegisterSerializer):
    address = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['address'] = self.validated_data.get('address', '')
        return data

    def save(self, request):
        user = super().save(request)
        user.address = self.cleaned_data.get('address')
        user.save()
        return user
