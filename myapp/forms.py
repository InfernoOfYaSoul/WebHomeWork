from django import forms

from .models import Info

class PostForm(forms.ModelForm):

    class Meta:
        model = Info
        fields = ('title', 'text',)