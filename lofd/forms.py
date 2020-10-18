from django.forms import ModelForm, ModelMultipleChoiceField, TextInput
from django import forms
from multiselectfield import MultiSelectField

from lofd.models import (
    Book,
    Watch,
    BookComment,
    WatchComment,
    Personal,
)

# Book List Create
class ListForm(ModelForm):
    class Meta:
        model = Book
        fields = ['authors', 'title', ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'input',
            }),
            'authors': TextInput(attrs={
                'class': 'input',
            }),
        }

# Watch List Create
class WatchForm(ModelForm):
    class Meta:
        model = Watch
        fields = ['title', 'cover_image' ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'input',
            }),
        }


class BookCommenForm(ModelForm):
    class Meta:
        model = BookComment
        fields = ['comments',]
        widgets = {
            'comments': TextInput(attrs={
                'class': 'input',
            }),
        }


class WatchCommenForm(ModelForm):
    class Meta:
        model = WatchComment
        fields = ['comments',]
        widgets = {
            'comments': TextInput(attrs={
                'class': 'input',
            }),
        }


class PersonForm(ModelForm):
    class Meta:
        model = Personal
        fields = ['name', 'surname', 'email', 'abouts', 'phone', 'f_account', 'i_account', 't_account']
        widgets = {
            'name': TextInput(attrs={
                'class': 'input',
            }),
            'surname': TextInput(attrs={
                'class': 'input',
            }),
            'email': TextInput(attrs={
                'class': 'input',
            }),
            'abouts': TextInput(attrs={
                'class': 'input',
            }),
            'phone': TextInput(attrs={
                'class': 'input',
            }),
            'f_account': TextInput(attrs={
                'class': 'input',
            }),
            'i_account': TextInput(attrs={
                'class': 'input',
            }),
            't_account': TextInput(attrs={
                'class': 'input',
            }),
        }