from django import forms
#from profiles.models import Profile, UserSkill
from .models import OpenClass, Category
from django.contrib.admin.widgets import AdminDateWidget # buat AdminDateInput


import datetime

#from profiles.models import Skill



def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')
"""
def must_be_last_max_guest(value):
    from .views import value_pk
    max_guest = Profile.objects.get(pk=value_pk()).user.maximum_guest
    if value > int(max_guest):
        raise forms.ValidationError('Guest melebihi kapasitas kelas')
"""
class OpenClassForm(forms.ModelForm):
    description = forms.CharField(required=True)
    fee = forms.IntegerField(required=False)
    location_name = forms.CharField(required=True)
    location_latitude = forms.CharField(required=True)
    location_longitude = forms.CharField(required=True)
    categories = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = OpenClass
        fields = (
            'description',
            'location_name',
            'location_latitude',
            'location_longitude',
            'categories',
            'fee',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder':'Example : di open class saya, kamu dapat berkonsultasi mengenai Fisika Dasar perkuliahan. Di open class saya dapat menjadi mentor Taekwondo'
        })
        self.fields['fee'].widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder':'Dalam IDR. isi 0 untuk membuka kelas secara gratis'
        })
        self.fields['location_latitude'].widget = forms.HiddenInput(attrs={'id':'formLat'})
        self.fields['location_longitude'].widget = forms.HiddenInput(attrs={'id':'formLon'})
        self.fields["location_name"].widget = forms.HiddenInput(attrs={'id':'formAddress'})

class OpenClassEditForm(forms.ModelForm):
    is_active = forms.BooleanField(required=False)
    class Meta:
        model = OpenClass
        fields = (
            'is_active',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget = forms.CheckboxInput(attrs={'id':'switch-1','class':'switch'})
   
class TagForm(forms.Form):
    tag = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-tag'}))

class BaseTagFormSet(forms.BaseFormSet):
    
    def clean(self):
        if any(self.errors):
            return

        tags = []
        
        if len(self.forms) > 5:
            raise forms.ValidationError("Maksimum tag 5")

        for form in self.forms:
            if form.cleaned_data:
                tag = form.cleaned_data['tag']

                if tag in tags:
                    raise forms.ValidationError("Tidak boleh ada tag yang duplikat")
                    
                tags.append(tag)
