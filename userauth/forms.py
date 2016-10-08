from django import forms
from auth.models import UserProfile, User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # username = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class UserProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender')
    def __init__(self, *args, **kwargs):
        super(UserProfileRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class UserProfileForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = UserProfile
        fields = ('gender', 'desc', 'business')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class ChangePWForm(forms.ModelForm):
    password = forms.CharField(label="Old password", widget=forms.PasswordInput(), max_length=100)
    new_pw = forms.CharField(label="New password", widget=forms.PasswordInput(), max_length=100)
    confirm_pw = forms.CharField(label="Confirm password", widget=forms.PasswordInput(), max_length=100)

    class Meta:
        model = User
        fields = ('password', 'new_pw', 'confirm_pw')
    def __init__(self, *args, **kwargs):
        super(ChangePWForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('auth:edit_settings')
        self.helper.add_input(Submit('submit', 'Change Password'))
        Layout(
            Fieldset(
                'Change Password',
                'password',
                'new_pw',
                'confirm_pw',

            ),
            Div(
                'password', 'new_password',
                title="top kek",
                style="background:black; color: red",
            )
        )