from django.urls import path
from lofd.views import *


urlpatterns = [
    path('', Home, name='index'),
    path('about/', About, name='about'),
    path('books/', BooksIndex, name='books'),
    path('watch/', WatchingIndex, name='watch'),
    path('lists/', Lists, name='lists'),
    path('mycomments/', mycCmments, name='mycomments'),
    path('create/', CreateWatchList, name='create'),
    path('add/<int:pid>', addList, name='add'),
    path('addWatch/<int:pid>', addWatch, name='addWatch'),
    path('booksDelete/<int:pid>', booksDelete, name='booksDelete'),
    path('watchDelete/<int:pid>', watchDelete, name='watchDelete'),

    path('createComment/<int:pid>', createComment, name='createComment'),
    path('createWComment/<int:pid>', createWComment, name='createWComment'),

    path('addComment/<int:pid>', addComment, name='addComment'),
    path('addWComment/<int:pid>', addWComment, name='addWComment'),
    path('booksCDelete/<int:pid>', booksCDelete, name='booksCDelete'),
    path('watchCDelete/<int:pid>', watchCDelete, name='watchCDelete'),

]
