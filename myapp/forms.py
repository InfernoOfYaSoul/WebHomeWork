from django import forms

from .models import *

class NameForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["photo"].required = True
        # self.fields["sex"].required = True
        # self.fields["sex"].choices = CHOICES
        self.fields["birth_date"].required = True
        self.fields["name"].label = ""
        self.fields["name"].required = True
        # self.fields["tg"].initial="@"
        self.fields["tg"].required = True
        self.fields["phone_num"].required = True
        
        
        #Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))

        


    class Meta:
        model = Info
        fields = ["photo", "sex1", "sex2", "birth_date", "name", "tg", "phone_num", "text"]
        # CHOICES = [(1, 1), (2, 2)]
        widgets = {
            "photo": forms.FileInput(attrs = {"class": "center-left-ava-download-button-input", "onchange": "gotPhoto(this)", "accept": "image/jpeg, image/png"}),
            # "sex": forms.RadioSelect(attrs = {'name': 'gender', "class": "custom-radio"}, choices=CHOICES),
            "sex1": forms.Select(attrs = {'name': 'gender', "class": "custom-radio", "id": "male"}),
            "sex2": forms.Select(attrs = {'name': 'gender', "class": "custom-radio", "id": "female"}),
            "birth_date": forms.TextInput(attrs = {"class": "inn", "name": "date", "id": "date", "placeholder": "Дата рождения", "onfocus": "(this.type='date')", "onblur": "(this.type='text')"}),
            "name": forms.TextInput(attrs = {"class": "inn", "name": "Name", "id": "name"}),  
            "tg": forms.TextInput(attrs = {"class": "inn", "name": "tg", "id": "name", "placeholder": "@telegram"}),
            "phone_num": forms.TextInput(attrs = {"class": "inn", "type": "text", "name": "phonenum", "id": "name", "placeholder": "Введите номер"}),
            "text": forms.TextInput(attrs = {"name": "infobox", "id": "infobox"}),
        }

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Info
#         fields = ('title', 'text',)