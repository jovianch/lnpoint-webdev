from django import forms

from accounts.models import User
from profiles.models import Profile

def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', 'jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Not image file extension')


class ContactUsForm(forms.Form):
    nama = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Verifikasi Email")
    question = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                            'placeholder':
        'isi pertanyaan kamu, ex: saya ingin mengajukan keahlian untuk belajar astrophysics apakah bisa? bagaimana keamanan bertransaksi di lnpoint?'}),
                               label='Pertanyaan atau Saran')
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="",
                               validators=[must_be_empty]
                               )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nama"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                             })
        self.fields["email"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                             })
        self.fields["verify_email"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder':'tulis email kembali'})


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "Kamu harus memasukan email dan verifikasi email yang sama")

class TemporaryForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("phone_number",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone_number"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder':"Isi no handphonemu yang dapat hubungi","id":"phoneNumber"})

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')

        numbers = ['0','1','2','3','4','5','6','7','8','9']

        for i in phone_number:
            if i not in numbers:
                raise forms.ValidationError(
                "No handphone harus berupa angka")

class AddAvatarForm(forms.ModelForm):
    avatar = forms.FileField(required=True, widget= forms.FileInput, validators=[validate_file_extension])

    class Meta:
        model = Profile
        fields = ('avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget = forms.FileInput(attrs={'id':'id_act_img',
                                                            'name':'act_img',
                                                            'style':""'display:none;'"",
                                                            'type':'file',
                                                            'accept':'image/*',
                                                            },)