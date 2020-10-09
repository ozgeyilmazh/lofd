from django.forms import ModelForm, ModelMultipleChoiceField, TextInput
from django import forms
from multiselectfield import MultiSelectField

from lofd.models import (
    Book,
    Watch,
    BookComment,
    WatchComment,
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