from django.urls import path
from lofd.views import *


urlpatterns = [
    path('', Home, name='index'),
    path('about/', About, name='about'),

    # Personal Read and Watch List
    path('books/', BooksIndex, name='books'),
    path('watch/', WatchingIndex, name='watch'),

    # Genele Açık Olan Kitap Listesi
    path('lists/', Lists, name='lists'),
    path('wlists/', WLists, name='wlists'),

    # Personal Comments
    #path('mycomments/', mycCmments, name='mycomments'),

    path('create/', CreateWatchList, name='create'),

    # Book Add
    path('add/<int:pid>', addList, name='add'),
    # Book Delete
    path('booksDelete/<int:pid>', booksDelete, name='booksDelete'),

    # Watch Add
    path('addWatch/<int:pid>', addWatch, name='addWatch'),
    # Watch Delete
    path('watchDelete/<int:pid>', watchDelete, name='watchDelete'),

    path('createComment/<int:pid>', createComment, name='createComment'),
    path('createWComment/<int:pid>', createWComment, name='createWComment'),

    path('updateComment/<int:pid>', updateComment, name='updateComment'),
    path('editComment/<int:pid>', editComment, name='editComment'),

    path('addComment/<int:pid>', addComment, name='addComment'),
    path('addWComment/<int:pid>', addWComment, name='addWComment'),
    #path('booksCDelete/<int:pid>', booksCDelete, name='booksCDelete'),
    #path('watchCDelete/<int:pid>', watchCDelete, name='watchCDelete'),


]
