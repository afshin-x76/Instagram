from .models import User
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, AuthenticationForm
    )

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'date_of_birth', 'profile_picture')
