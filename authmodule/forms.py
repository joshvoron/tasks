from django.forms import ModelForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=True)
        return user

class UserDeleteForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('password',)


class ChangeEmailForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class UserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_photo')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class ChangePasswordForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('password',)
