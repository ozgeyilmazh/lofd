from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from lofd.forms import (
	ListForm,
	WatchForm,
	BookCommenForm,
	WatchCommenForm,
)
from lofd.models import (
	Book,
	BookUserList,
	Watch,
	WatchUserList,
	BookComment,
	WatchComment,
	#Peronal,
)
from django.contrib import messages
from django.http import HttpResponse, response, request, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import ListView

def Home(request):
	context = dict()
	context['items'] = "Onder"

	template = 'index.html'
	return render(request, template, context)


def About(request):
	context = dict()
	#context['personal'] = Peronal.objects.all()

	template = 'about.html'
	return render(request, template, context)


def BooksIndex(request):
	context = dict()
	currentUser = request.user.id

	# Books Lists & Pagination
	books = BookUserList.objects.filter(user_id=currentUser)
	paginator = Paginator(books, 10)

	c = BookComment.objects.filter(user_id=currentUser)


	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		context['books'] = paginator.page(page)
		context['c'] = c

	except(EmptyPage):
		context['books'] = paginator.page(paginator.num_pages)
		context['c'] = c

	template = 'books.html'
	return render(request, template, context)


def WatchingIndex(request):
	context = dict()
	currentUser = request.user.id
	watch = WatchUserList.objects.filter(user_id=currentUser)
	paginator = Paginator(watch, 10)

	w = WatchComment.objects.filter(user_id=currentUser)


	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		context['watch'] = paginator.page(page)
		context['w'] = w

	except(EmptyPage):
		context['watch'] = paginator.page(paginator.num_pages)
		context['w'] = w


	template = 'watches.html'
	return render(request, template, context)


def Lists(request):
	context = dict()
	# Books Lists & Pagination
	bookLists = Book.objects.all()
	paginator = Paginator(bookLists, 20)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		context['books'] = paginator.page(page)
	except(EmptyPage):
		context['books'] = paginator.page(paginator.num_pages)

	# Watch Lists & Pagination
	watchLists = Watch.objects.all()
	paginator = Paginator(watchLists, 20)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		context['watch'] = paginator.page(page)
	except(EmptyPage):
		context['watch'] = paginator.page(paginator.num_pages)


	template = 'lists.html'
	return render(request, template, context)


def CreateWatchList(request):
	context = dict()
	url = request.META.get('HTTP_REFERER')

	if request.method == 'POST':

		return HttpResponseRedirect(url)

	template = 'lists.html'
	return render(request, template, context)

"""
def mycCmments(request):
	context = dict()
	currentUser = request.user.id
	context['commentsB'] = BookComment.objects.filter(user_id=currentUser)
	context['commentsW'] = WatchComment.objects.filter(user_id=currentUser)

	template = 'mycomments.html'
	return render(request, template, context)
"""

# Müşteri Sepet Onaylama
def addList(request, pid):
	context = dict()
	url = request.META.get('HTTP_REFERER')

	current_user = request.user
	form = ListForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			print("Form 1")
			data = BookUserList()
			data.user = current_user
			data.authors = form.cleaned_data['authors']
			data.title = form.cleaned_data['title']
			try:
				q1 = BookUserList.objects.get(user_id=current_user.id, booksList_id=pid)
			except BookUserList.DoesNotExist:
				q1 = None
			if q1 != None:
				messages.success(request, ' This book is already added')
			else:
				data.booksList_id = pid
				#data.booksList_id = BookUserList(user_id=current_user.id, pk=pid)
				data.save()
				messages.success(request, ' Thank You')
		return HttpResponseRedirect(url)

	template = 'lists.html'
	return render(request, template, context)


def addWatch(request, pid):
	context = dict()
	url = request.META.get('HTTP_REFERER')

	current_user = request.user
	form2 = WatchForm(request.POST or None)
	if request.method == 'POST':
		if form2.is_valid():
			print("Form 2")
			data2 = WatchUserList()
			data2.user = current_user
			data2.cover_image = form2.cleaned_data['cover_image']
			data2.title = form2.cleaned_data['title']
			try:
				q1 = WatchUserList.objects.get(user_id=current_user.id, watchesList_id=pid)
			except WatchUserList.DoesNotExist:
				q1 = None
			if q1 != None:
				messages.success(request, ' This watch is already added')
			else:
				data2.watchesList_id = pid
				data2.save()
				messages.success(request, ' Thank You')
		return HttpResponseRedirect(url)


	template = 'lists.html'
	return render(request, template, context)


def createComment(request, pid):
	context = dict()
	context['books'] = get_object_or_404(Book, id=pid)

	template = 'comments/text.html'
	return render(request, template, context)


def updateComment(request, pid):
	context = dict()
	context['book'] = get_object_or_404(Book, id=pid)

	books = get_object_or_404(BookComment, booksList_id=pid)
	booksName = get_object_or_404(BookUserList, booksList_id=pid)
	#context['books'] = books.comments
	form = BookCommenForm(request.POST or None, instance=books)
	if form.is_valid():
		form.save()

		return redirect('books')

	context['books'] = books
	context['booksName'] = booksName

	template = 'comments/updateText.html'
	return render(request, template, context)


def editComment(request, pid):
	context = dict()
	posts = get_object_or_404(BookComment, booksList_id=pid)

	if request.method == "POST":
		form = BookComment(request.POST or None, instance=posts)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = request.user
			post.comments = form.comments
			post.save()
			context['books'] = posts

			template='books.html'
			return render(request, template, context)
	else:
		context['books'] = BookCommenForm(instance=posts)

	template='books.html'
	return render(request, template, context)


def createWComment(request, pid):
	context = dict()
	context['watch'] = get_object_or_404(Watch, id=pid)

	template = 'comments/text.html'
	return render(request, template, context)

# Book Comments
def addComment(request, pid):
	context = dict()
	current_user = request.user
	form2 = BookCommenForm(request.POST or None)
	if request.method == 'POST':
		if form2.is_valid():
			data2 = BookComment()
			data2.user = current_user
			data2.comments = form2.cleaned_data['comments']
			try:
				q1 = BookComment.objects.get(user_id=current_user.id, booksList_id=pid)
				print("q1 yorum var", q1)
			except BookComment.DoesNotExist:
				q1 = None
				print("except çalıştı")
			if q1 != None:
				messages.success(request, ' This book comments is already added')
			else:
				data2.booksList_id = pid
				data2.save()
				messages.success(request, ' Thank You')
		return HttpResponseRedirect("/books")

	template = 'books.html'
	return render(request, template, context)


# Watch Comments
def addWComment(request, pid):
	context = dict()
	current_user = request.user
	form = WatchCommenForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			print("Form 2")
			data = WatchComment()
			data.user = current_user
			data.comments = form.cleaned_data['comments']

			try:
				q1 = WatchComment.objects.get(user_id=current_user.id, watchesList_id=pid)
			except WatchComment.DoesNotExist:
				q1 = None
			if q1 != None:
				messages.success(request, ' This book comments is already added')
			else:
				data.watchesList_id = pid
				data.save()
				messages.success(request, ' Thank You')
		return HttpResponseRedirect("/watch")

	template = 'watches.html'
	return render(request, template, context)


# Listeden Kitap Silme
def booksDelete(request, pid):
	url = request.META.get('HTTP_REFERER')
	try:
		# Sil Bilgisi gelen kitabın id bilgisi ile yorum modelinden karşılığı çekip silme işlemi gerçekleşiyor
		gelen = get_object_or_404(BookUserList, id=pid)
		which = gelen.booksList_id
		bookCDelete = get_object_or_404(BookComment, booksList_id=which)
		# Listeden kitap silme
		BookUserList.objects.filter(id=pid).delete()

		# Yapılan yorumun Silinmesi
		BookComment.objects.filter(id=bookCDelete.pk).delete()
	except:
		# Listeden kitap silme
		BookUserList.objects.filter(id=pid).delete()
	current_user = request.user
	request.session['books'] = BookUserList.objects.filter(user_id=current_user.id).count()
	messages.success(request, "BookUserList deleted from .. ")
	return HttpResponseRedirect(url)


# Listeden izleme Silme
def watchDelete(request, pid):
	url = request.META.get('HTTP_REFERER')
	try:
		# Sil Bilgisi gelen izlemenin id bilgisi ile yorum modelinden karşılığı çekip silme işlemi gerçekleşiyor
		gelen = get_object_or_404(WatchUserList, id=pid)
		which = gelen.watchesList_id
		watchCDelete = get_object_or_404(WatchComment, watchesList_id=which)
		# İzleme bilgisinin Silinmesi
		WatchUserList.objects.filter(id=pid).delete()
		# Yapılan yorumun Silinmesi
		WatchComment.objects.filter(id=watchCDelete.pk).delete()

	except:
		# İzleme bilgisinin Silinmesi
		WatchUserList.objects.filter(id=pid).delete()

	current_user = request.user
	request.session['books'] = WatchUserList.objects.filter(user_id=current_user.id).count()
	messages.success(request, "WatchUserList deleted from .. ")
	return HttpResponseRedirect(url)

""" Bu işlemi bu booksDelete fonksiyondan kitap ile beraber yorum silme 
# Listeden Kitap Yorum Silme
def booksCDelete(request, pid):
	url = request.META.get('HTTP_REFERER')
	BookComment.objects.filter(id=pid).delete()
	current_user = request.user
	request.session['books'] = BookComment.objects.filter(user_id=current_user.id).count()
	messages.success(request, "BookComment deleted from .. ")
	return HttpResponseRedirect(url)
"""
""" Bu işlemi bu watchDelete fonksiyondan İzleme ile beraber yorum silme 
# Listeden Dizi Film Yorum Silme
def watchCDelete(request, pid):
	url = request.META.get('HTTP_REFERER')
	WatchComment.objects.filter(id=pid).delete()
	current_user = request.user
	request.session['books'] = WatchComment.objects.filter(user_id=current_user.id).count()
	messages.success(request, "WatchComment deleted from .. ")
	return HttpResponseRedirect(url)
"""


def error_404(request, exception):
	context = dict()
	context['info'] = "Aradığınız sayfa bulunamadı"
	return render(request,'error/error_404.html', context)

def error_500(request):
	context = dict()

	return render(request,'error/error_500.html', context)