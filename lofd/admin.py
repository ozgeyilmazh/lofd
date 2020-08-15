from django.contrib import admin
from .models import (
    Book,
    Watch,
    BookUserList,
    WatchUserList,
    BookComment,
    WatchComment,
)
# Ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from import_export.admin import ImportExportModelAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'authors',
        'title',
    )


class WatchAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
    )


class BookUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
    )


class WatchUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
    )



class BookCommentUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'booksList',
        'comments',
    )




class WatchCommentUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'watchesList',
        'comments',
    )

# Ckeditor
class ModalClass:
    content = RichTextUploadingField()

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())


admin.site.register(BookUserList, BookUserAdmin)
admin.site.register(WatchUserList, WatchUserAdmin)
admin.site.register(BookComment, BookCommentUserAdmin)
admin.site.register(WatchComment, WatchCommentUserAdmin)


admin.site.register(Book, BookAdmin)
admin.site.register(Watch, WatchAdmin)
