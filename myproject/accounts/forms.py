from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.core.validators import validate_email

class SignupForm(UserCreationForm):
    # User에 없는 필드 추가
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)
        return value
        
    def save(self):
        user = super().save()
        Profile.objects.create(user=user, 
                                phone_number = self.cleaned_data['phone_number'],
                                address = self.cleaned_data['address'])
        return user
                                
                                
