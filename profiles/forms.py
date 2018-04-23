from django import forms
from django.forms.formsets import BaseFormSet
from django.core.validators import RegexValidator


from .models import Profile
from accounts.models import User

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', 'jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Not image file extension')

class EditProfileForm(forms.ModelForm):

    avatar = forms.FileField(required=False, widget= forms.FileInput, validators=[validate_file_extension])
    bio = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ('avatar', 'bio')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget = forms.FileInput(attrs={'style':""'max-width:95px;'"",
                                                                'accept':'image/*',})
        self.fields['bio'].widget = forms.TextInput(attrs={'class': 'form-control',})

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
        "fullname",
        #"username",
        "contact", 
        "institution",
        "phone_number"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["username"].widget = forms.TextInput(attrs={'placeholder': "Username"})
        self.fields["fullname"].widget = forms.TextInput(attrs={'placeholder': "Full Name"})
        #self.fields["username"].validators = [RegexValidator(r'^[A-Za-z0-9_.]+$',
        #                                                     message="Hanya alphanumerik, garis bawah,dan titik yang diperbolehkan")]
        self.fields["fullname"].validators = [RegexValidator(r'^[A-za-z ]+$',
                                                             message="Hanya huruf dan spasi yang diperbolehkan")]
        #self.fields["username"].widget = forms.TextInput(attrs={'class': 'form-control',
        #                                                           'placeholder':'Username'})
        self.fields["fullname"].widget = forms.TextInput(attrs={'class': 'form-control form-fullname',
                                                                   'placeholder':'Nama Lengkap',})
        self.fields["institution"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder':'Institusi Pendidikan Anda'})
        self.fields["contact"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder':"Kontak ( LINE )"})
        self.fields["phone_number"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder':"No handphone yang dapat hubungi"})
        



"""
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['skill'] = forms.ChoiceField(
            choices=[(s.name) for name in Skill.objects.all()]
        )
"""
