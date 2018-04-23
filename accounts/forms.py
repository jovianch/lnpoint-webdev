from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import RegexValidator
from django import forms
from .models import User
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate



class SignUpForm(UserCreationForm):

    class Meta:
        fields = ("username", "email", "fullname", "phone_number", "password1", "password2")
        model = get_user_model()

    def clean_username(self):
        return self.cleaned_data["username"].lower()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].validators = [RegexValidator(r'^[A-Za-z0-9_.]+$',
                                                             message="Hanya alphanumerik, garis bawah,dan titik yang diperbolehkan")]
        self.fields["fullname"].validators = [RegexValidator(r'^[A-za-z ]+$',
                                                             message="Hanya huruf dan spasi yang diperbolehkan")]
        self.fields["username"].widget = forms.TextInput(attrs={'placeholder': "Username"})
        self.fields["phone_number"].widget = forms.TextInput(attrs={'placeholder': "Phone Number"})
        self.fields["email"].widget = forms.TextInput(attrs={'placeholder':"Email"})
        self.fields["fullname"].widget = forms.TextInput(attrs={'placeholder': "Full Name"})
        self.fields["password1"].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields["password2"].widget = forms.PasswordInput(attrs={'placeholder': "Password Confirmation"})

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')

        numbers = ['0','1','2','3','4','5','6','7','8','9']

        for i in phone_number:
            if i not in numbers:
                raise forms.ValidationError(
                "No handphone harus berupa angka")

        if len(phone_number) < 8:
            raise forms.ValidationError(
                "No handphone harus di atas 7 digit (indonesia)"
            )


    # after save(), signal sent to create new profile


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].validators = [RegexValidator(r'^[A-za-z0-9_]+$',
                                                             message="Invalid username or password, please try again")]
        self.fields["username"].widget = forms.TextInput(attrs={'placeholder': 'Usernames'})
        self.fields["password"].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})

    def clean_username(self):
        return self.cleaned_data['username'].lower()


class VerifyForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("card_id", "contact",  "institution", "phone_number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["institution"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder':'Institusi Pendidikan Anda'})
        self.fields["contact"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder':"Kontak ( LINE )"})
        self.fields["card_id"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': "Nomor NIM"})
        self.fields["phone_number"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder':"No handphone yang dapat hubungi"})
        self.fields["card_id"].validators = [RegexValidator(r'^[0-9]+$', message="Invalid NIM Format")]
        self.fields["card_id"].label = "ID Card"



class ChangePasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__( *args, **kwargs)

        self.fields['current_password'] = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'placeholder': 'Password Lama'
            })
        )
        self.fields['new_password'] = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'placeholder': 'Password Baru'
            })
        )
        self.fields['new_password2'] = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'placeholder': 'Password Baru, Lagi'
            })
        )

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']

        if not self.user.check_password(current_password):
            raise forms.ValidationError('Password lama salah, Silahkan coba lagi')
        else:
            pass

    def clean_new_password2(self):
        password1 = self.cleaned_data['new_password']
        password2 = self.cleaned_data['new_password2']

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    'Password pertama dan kedua tidak cocok ')
        else:
            pass


class AccountCloseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['password1'] = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'placeholder':'Password'
            }),
            error_messages={
                'required':'Masukkan password baru'
            }
        )

    def clean_password(self):
        password = self.cleaned_data('password1')

        if not self.user.check_password(password):
            raise forms.ValidationError("Password Salah, Silahkan coba lagi")
        else:
            pass
