import datetime
from django import forms
from django.forms.widgets import SelectDateWidget

from .widgets import BootstrapTimeWidget
from .models import Activity

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', 'jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Not image file extension')


class ActivityDoneForm(forms.ModelForm):
    caption = forms.CharField(required=True)
    photo = forms.FileField(required=True, widget= forms.FileInput, validators=[validate_file_extension])

    class Meta:
        model = Activity
        fields = (
        'photo',
        'caption',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['photo'].widget = forms.FileInput(attrs={'id':'id_act_img',
                                                            'name':'act_img',
                                                            'style':""'display:none;'"",
                                                            'type':'file',
                                                            'accept':'image/*',
                                                            },)
        self.fields["caption"].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'cols':'40', 
            'rows':'5',
            'id':'id_act_description',
            'name':'description',
            'placeholder':'Write caption here... ',
            'value':'-'
        })



class ActivityForm(forms.ModelForm):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    location_name = forms.CharField(required=True)
    location_latitude = forms.CharField(required=True)
    location_longitude = forms.CharField(required=True)
    maximum_guest = forms.CharField(required=True)
    fee = forms.IntegerField(required=False)
    duration = forms.IntegerField(required=True)
    date_held = forms.DateField(required=True,  widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),attrs={'class':'form-control'}
    ),)
    time = forms.TimeField(input_formats=['%H:%M', '%H:%M:%S'],
            required=False)
    
    class Meta:
        model = Activity
        fields = (
        #Basic Info
        'name',
        'description',
        'maximum_guest',
        'fee',
        #Time
        'duration',
        'date_held',
        'time',
        #from API
        'location_latitude',
        'location_longitude',
        'location_name'
        )

    def clean_date_held(self):
        data = self.cleaned_data['date_held']
        if data < datetime.datetime.now().date():
            raise forms.ValidationError("You cant held activity in the past")
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["time"].widget = forms.TextInput(attrs={'class': 'form-control',})
        self.fields["name"].widget = forms.TextInput(attrs={
            'id':'name',
            'placeholder':'Contoh: Belajar bareng sebelum UTS Fisika TPB'
        })
        self.fields["description"].widget = forms.Textarea(attrs={
            'class': 'materialize-textarea',
            'tabindex':'12',
            'rows':'10',
            'id':'description',
            'placeholder':'Tuliskan apa yang ingin kamu lakukan diaktivitasmu! Contoh: Di kelas ini kita akan membahas Matcho Bab II'
        })
        self.fields["maximum_guest"].widget = forms.NumberInput(attrs={'id': 'guest',
                                                                     'placeholder': 'Jumlah peserta  maksimum kelas'})
        self.fields["fee"].widget = forms.NumberInput(attrs={'id': 'price',
                                                           'placeholder': 'Dalam IDR, isi 0 untuk membuat aktivitas secara gratis'})
        self.fields['location_latitude'].widget = forms.HiddenInput(attrs={'id':'formLat'})
        self.fields['location_longitude'].widget = forms.HiddenInput(attrs={'id':'formLon'})
        self.fields["location_name"].widget = forms.HiddenInput(attrs={'id':'formAddress'})
        self.fields["duration"].widget = forms.TextInput(attrs={'id':'duration'})
    



    





