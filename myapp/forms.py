from django import forms
from django.core.exceptions import ValidationError
from .models import *

choice_sex = [
    ('M', 'Парень'),
    ('F', 'Девушка'),
]

choice_stud = [
    ('S', 'Студент / выпускник'),
    ('T', 'Сотрудник'),
]

choice_step = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
]

choice_ed_step = [
    ('bachelor', 'Бакалавриат'),
    ('magistracy', 'Магистратура'),
    ('postgraduate', 'Аспирантура'),
]

class NameForm(forms.ModelForm):

    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["photo"].required = False
        self.fields["birth_date"].required = False
        self.fields["name"].label = ""
        self.fields["phone_num"].initial = "+7"
        self.fields["phone_num"].required = False
        self.fields["name"].required = False
        self.fields["tg"].required = False
        self.fields["student"].required = False
        self.fields["step"].required = False
        self.fields["ed_step"].required = False
        

    class Meta:
        model = Info
        fields = [
            "photo", "sex", "birth_date", "name", "tg", "phone_num", "text", "student", "step", "ed_step" 
        ]
        widgets = {
            "photo": forms.FileInput(attrs = {"class": "center-left-ava-download-button-input", "onchange": "gotPhoto(this)", "accept": "image/jpeg, image/png"}),
            # "sex": forms.RadioSelect(attrs = {'name': 'gender', "class": "custom-radio"}, choices=choice_sex),
            # "sex1": forms.Select(attrs = {'name': 'gender', "class": "custom-radio", "id": "male"}),personal-info-txt
            # "sex2": forms.Select(attrs = {'name': 'gender', "class": "custom-radio", "id": "female"}),, "class": "custom-radio" 
            "sex": forms.RadioSelect(choices=choice_sex, attrs = {'name': 'gender', "class": "custom-r"}),
            "birth_date": forms.TextInput(attrs = {"class": "inn", "name": "date", "id": "date", "placeholder": "Дата рождения", "onfocus": "(this.type='date')", "onblur": "(this.type='text')"}),
            "name": forms.TextInput(attrs = {"class": "inn", "name": "Name", "id": "name"}),  
            "tg": forms.TextInput(attrs = {"class": "inn", "name": "tg", "id": "name", "placeholder": "@telegram"}),
            "phone_num": forms.TextInput(attrs = {"class": "inn", "type": "text", "name": "phonenum", "id": "name", "placeholder": "Введите номер"}),
            "text": forms.TextInput(attrs = {"name": "infobox", "id": "infobox"}),

            "student": forms.RadioSelect(choices=choice_stud, attrs = {'name': 'gender', "class": "custom-r"}),
            "step": forms.RadioSelect(choices=choice_step, attrs = {'name': 'gender', "class": "custom-r", "style": "displey:none"}),
            "ed_step": forms.Select(attrs = {"class": "personal-info-txt_dropbox"}, choices=choice_ed_step),
        }

    def clean_fields(self):
        photo = self.cleaned_data['photo']
        if photo is None:
            raise ValidationError("photo is null")

    

    

