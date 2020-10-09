from import_export import resources
from lofd.models import Book, Watch


class BooksResources(resources.ModelResource):

    class Meta:
        model = Book
        fields = (
            'id',
            'authors',
            'title',
        )



class WatchResources(resources.ModelResource):

    class Meta:
        model = Watch
        fields = (
            'id',
            'title',
        )