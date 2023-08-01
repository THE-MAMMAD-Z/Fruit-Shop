from django import forms
from accounts.models import Profile

class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username= forms.CharField( max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email= forms.EmailField(widget=forms.EmailInput)
    # phone = forms.IntegerField()
    # address= forms.TimeField()

    class Meta:
        model = Profile
        fields=['profileimage','Gender','phone','address']
    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profileimage','Gender','phone','address']


# class UserEditForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         fields=['profileimage','Gender','phone','address']
#     password=None
