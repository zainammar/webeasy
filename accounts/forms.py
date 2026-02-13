from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SimpleSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'password', 'phone', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

            # Create Profile
            Profile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address']
            )

        return user
