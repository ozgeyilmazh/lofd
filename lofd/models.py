from django import forms
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Ckeditor
from ckeditor_uploader.fields import RichTextUploadingField

# Book
from multiselectfield import MultiSelectField


class Book(models.Model):
    authors = models.CharField(
        max_length=200,
        default="",
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=200,
        default="",
        null=True,
        blank=True,
    )
    cover_image=models.ImageField(
        null=True,
        blank=True,
        upload_to='books',
    )
    #comment = RichTextField(verbose_name="Comment", default="")


    def __str__(self):
        return f" {self.authors} - {self.title} "


    class Meta:
        ordering = ['title']


# Movie & Series
class Watch(models.Model):
    title=models.CharField(
        max_length=200,
        default="",
        null=True,
        blank=True,
    )

    cover_image=models.ImageField(
        null=True,
        blank=True,
        upload_to='movies',
    )

    def __str__(self):
        return self.title


class BookUserList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    booksList = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        null=True,
    )


class WatchUserList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    watchesList = models.ForeignKey(
        Watch,
        on_delete=models.SET_NULL,
        null=True,

    )


class BookComment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    booksList = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,

    )
    comments = RichTextField(max_length=350)


class WatchComment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    watchesList = models.ForeignKey(
        Watch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,

    )

    comments = RichTextField(max_length=350)

"""
class Peronal(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    address = models.CharField(
        max_length=150,
        blank=True
    )
    phone = models.CharField(
        max_length=15,
        blank=True
    )
    email = models.CharField(
        max_length=30,
        blank=True
    )

    f_account = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    # Instagram Hesabı
    i_account = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    l_account = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    t_account=models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.phone,
"""