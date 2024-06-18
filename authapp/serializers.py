from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import NewUser

class NewRegisterSerializer(RegisterSerializer):
    home_address = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['home_address'] = self.validated_data.get('home_address', '')
        return data

    def save(self, request):
            user = super().save(request)
            user.home_address = self.cleaned_data.get('home_address')
            user.save()
            return user
    

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'home_address', 'favourite_facility']  # Add any other fields you want to include