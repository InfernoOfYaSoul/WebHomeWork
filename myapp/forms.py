from django import forms

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

class NameForm(forms.ModelForm):

    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["photo"].required = True
        self.fields["birth_date"].required = True
        self.fields["name"].label = ""
        self.fields["name"].required = True
        self.fields["tg"].required = True
        self.fields["phone_num"].required = True

        


    class Meta:
        model = Info
        fields = [
            "photo", "sex", "birth_date", "name", "tg", "phone_num", "text", "student", "step" 
        ]
        widgets = {
            "photo": forms.FileInput(attrs = {"class": "center-left-ava-download-button-input", "onchange": "gotPhoto(this)", "accept": "image/jpeg, image/png"}),
            # "sex": forms.RadioSelect(attrs = {'name': 'gender', "class": "custom-radio"}, choices=choice_sex),
            # "sex1": forms.Select(attrs = {'name': 'gender', "class": "custom-radio", "id": "male"}),
            # "sex2": forms.Select(attrs = {'name': 'gender', "class": "custom-radio", "id": "female"}),, "class": "custom-radio" 
            "sex": forms.RadioSelect(choices=choice_sex, attrs = {'name': 'gender', "class": "custom-r"}),
            "birth_date": forms.TextInput(attrs = {"class": "inn", "name": "date", "id": "date", "placeholder": "Дата рождения", "onfocus": "(this.type='date')", "onblur": "(this.type='text')"}),
            "name": forms.TextInput(attrs = {"class": "inn", "name": "Name", "id": "name"}),  
            "tg": forms.TextInput(attrs = {"class": "inn", "name": "tg", "id": "name", "placeholder": "@telegram"}),
            "phone_num": forms.TextInput(attrs = {"class": "inn", "type": "text", "name": "phonenum", "id": "name", "placeholder": "Введите номер"}),
            "text": forms.TextInput(attrs = {"name": "infobox", "id": "infobox"}),

            "student": forms.RadioSelect(choices=choice_stud, attrs = {'name': 'gender', "class": "custom-r"}),
            "step": forms.RadioSelect(choices=choice_step, attrs = {'name': 'gender', "class": "custom-r", "style": "displey:none"}),
        }

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Info
#         fields = ('title', 'text',)