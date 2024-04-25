from django import forms
from .models import Product, CustomUser
from django.contrib.auth.models import User
from .models import News

from django import forms

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'video']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'contact')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['description'].required = True
        self.fields['price'].required = True
        self.fields['image'].required = True
        self.fields['contact'].required = True



class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

class ContactForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('contact',)