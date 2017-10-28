from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('This user does not exist in our service')
        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password')

        if not user.is_active:
            raise forms.ValidationError('User is no longer active')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email2 = forms.EmailField(label='Confirm Email', required=True)
    username = forms.CharField( widget=forms.TextInput(),
        max_length=255)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
