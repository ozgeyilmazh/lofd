from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from lofd.forms import (
	ListForm,
	WatchForm,
	BookCommenForm,
	WatchCommenForm,
	PersonForm,
)
from lofd.models import (
	Book,
	BookUserList,
	Watch,
	WatchUserList,
	BookComment,
	WatchComment,
	Personal,
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
	context['personal'] = Personal.objects.all()

	template = 'about.html'
	return render(request, template, context)


def BooksIndex(request):
	context = dict()
	currentUser = request.user.id

	# Books Lists & Pagination
	books = BookUserList.objects.filter(user_id=currentUser)
	paginator = Paginator(books, 8)

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
	paginator = Paginator(watch, 8)

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
	paginator = Paginator(bookLists, 8)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		context['books'] = paginator.page(page)
	except(EmptyPage):
		context['books'] = paginator.page(paginator.num_pages)

	template = 'lists.html'
	return render(request, template, context)


def WLists(request):
	context = dict()

	# Watch Lists & Pagination
	watchLists = Watch.objects.all()
	paginator = Paginator(watchLists, 6)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		context['watch'] = paginator.page(page)
	except(EmptyPage):
		context['watch'] = paginator.page(paginator.num_pages)

	template = 'w-lists.html'
	return render(request, template, context)


"""
# Burası gereksiz Silinebilir
def CreateWatchList(request):
	context = dict()
	url = request.META.get('HTTP_REFERER')

	if request.method == 'POST':

		return HttpResponseRedirect(url)

	template = 'lists.html'
	return render(request, template, context)
"""


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
				print("try")
			except BookUserList.DoesNotExist:
				q1 = None
				print("except")

			if q1 != None:
				messages.success(request, ' This book is already added')
				print("if")
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
	print("trydan önce")
	try:
		q1 = get_object_or_404(BookComment, booksList_id=pid)
		print("try")
	except:
		q1 = None
		print("except")
	if q1 != None:
		print("if")
		context['bComments'] = get_object_or_404(BookComment, booksList_id=pid)

		template='comments/updateText.html'
		return render(request, template, context)

	else:
		template='comments/text.html'
		return render(request, template, context)

	template = 'comments/text.html'
	return render(request, template, context)


# books için update yorum işlemi
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


# watches için update yorum işlemi
def editComment(request, pid):
	context = dict()
	context['watch'] = get_object_or_404(Watch, id=pid)

	watches = get_object_or_404(WatchComment, watchesList_id=pid)
	watchName = get_object_or_404(WatchUserList, watchesList_id=pid)
	#context['books'] = books.comments
	form = WatchCommenForm(request.POST or None, instance=watches)
	if form.is_valid():
		form.save()

		return redirect('watch')

	context['watches'] = watches
	context['watchName'] = watchName

	template = 'comments/updateText.html'
	return render(request, template, context)


# watches için Create yorum işlemi
def createWComment(request, pid):
	context = dict()
	context['watch'] = get_object_or_404(Watch, id=pid)
	print("trydan önce")
	try:
		q1 = get_object_or_404(WatchComment, watchesList_id=pid)
		print("try")
	except:
		q1 = None
		print("except")
	if q1 != None:
		print("if")
		context['wComments'] = get_object_or_404(WatchComment, watchesList_id=pid)

		template='comments/updateText.html'
		return render(request, template, context)

	else:
		template = 'comments/text.html'
		return render(request, template, context)

	template = 'books.html'
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

				watches=get_object_or_404(WatchComment, watchesList_id=pid)
				watchName=get_object_or_404(WatchUserList, watchesList_id=pid)
				# context['books'] = books.comments
				form=WatchCommenForm(request.POST or None, instance=watches)
				if form.is_valid():
					form.save()

					return redirect('watch')

				context['watches']=watches
				context['watchName']=watchName
				template='comments/updateText.html'
				return render(request, template, context)
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



def personIndex(request):
	context = dict()
	current_user = request.user
	#context['users'] = get_object_or_404(User, id=current_user.id)
	print("trydan önce")
	print(get_object_or_404(User, id=current_user.id))
	print("*************")
	try:
		q1 = get_object_or_404(Personal, user_id=current_user.id)
		print("q1", q1)
		print("try")
	except:
		q1 = None
		print("except")
		print("q1", q1)

	if q1 != None:
		print("if")
		context['userInfo'] = get_object_or_404(Personal, user_id=current_user.id)

		template = 'personEdit.html'
		return render(request, template, context)
	else:

		template = 'person.html'
		return render(request, template, context)

	template = 'person.html'
	return render(request, template, context)

	"""

	context = dict()
	url = request.META.get('HTTP_REFERER')

	current_user = request.user
	if request.method == 'POST':
		form = PersonForm(request.POST or None)
		if form.is_valid():
			data = form.save(commit=False)
			data.user = current_user
			data.name = form.cleaned_data['name']
			data.surname = form.cleaned_data['surname']
			data.email = form.cleaned_data['email']
			data.abouts = form.cleaned_data['abouts']
			data.phone = form.cleaned_data['phone']
			data.f_account = form.cleaned_data['f_account']
			data.i_account = form.cleaned_data['i_account']
			data.t_account = form.cleaned_data['t_account']
			data.save()
		else:
			context['form'] = PersonForm(request.POST)

		return HttpResponseRedirect(url)

			try:
				q1 = Peronal.objects.get(user_id=current_user.id)
				print("try")
			except BookUserList.DoesNotExist:
				q1 = None
				print("except")

			if q1 != None:
				messages.success(request, ' This book is already added')
				print("if")
			else:
				data.booksList_id = pid
				#data.booksList_id = BookUserList(user_id=current_user.id, pk=pid)
				data.save()
				messages.success(request, ' Thank You')
		return HttpResponseRedirect(url)
	template = 'person.html'
	return render(request, template, context)
	"""


def personEdit(request):
	context = dict()

	current_user = request.user

	post = get_object_or_404(User, pk=current_user.id)
	puser = get_object_or_404(Personal, user_id=post.id)
	puserU = get_object_or_404(Personal, user_id=post.id)
	if request.method == "POST":
		form = PersonForm(request.POST or None, instance=puser)
		if form.is_valid():
			puser = form.save(commit=False)
			puser.user = current_user
			if form.cleaned_data['name']:
				puser.name = form.cleaned_data['name']
				print("name var")
			else:
				puser.name = puserU.name
				print("name yok")
			if form.cleaned_data['surname']:
				puser.surname = form.cleaned_data['surname']
				print("name var")
			else:
				puser.surname = puserU.surname
				print("name yok")

			if form.cleaned_data['email']:
				print("burada email var")
				puser.email = form.cleaned_data['email']
			else:
				puser.email = puserU.email
				print(puserU.email)
				print("burada email boştu")
			if form.cleaned_data['abouts']:
				print("burada abouts var")
				puser.abouts = form.cleaned_data['abouts']
			else:
				puser.abouts = puserU.abouts
				print(puserU.email)
				print("burada abouts boştu")

			if form.cleaned_data['phone']:
				print("burada phone var")
				puser.phone = form.cleaned_data['phone']
			else:
				puser.phone = puserU.phone
				print(puserU.phone)
				print("burada phone boştu")

			if form.cleaned_data['f_account']:
				print("burada f_account var")
				puser.f_account = form.cleaned_data['f_account']
			else:
				puser.f_account = puserU.f_account
				print(puserU.f_account)
				print("burada f_account boştu")

			if form.cleaned_data['i_account']:
				print("burada i_account var")
				puser.i_account = form.cleaned_data['i_account']
			else:
				puser.i_account = puserU.i_account
				print(puserU.i_account)
				print("burada i_account boştu")

			if form.cleaned_data['t_account']:
				print("burada t_account var")
				puser.t_account = form.cleaned_data['t_account']
			else:
				puser.t_account = puserU.t_account
				print(puserU.t_account)
				print("burada t_account boştu")

			puser.save()

			return redirect('about')


	context['users'] = puser
	"""
	if request.method == "POST":
		form = PersonForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.name = form.cleaned_data['name']
			post.surname = form.cleaned_data['surname']
			post.email = form.cleaned_data['email']
			post.abouts = form.cleaned_data['abouts']
			post.phone = form.cleaned_data['phone']
			post.f_account = form.cleaned_data['f_account']
			post.i_account = form.cleaned_data['i_account']
			post.t_account = form.cleaned_data['t_account']
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PersonForm(instance=post)
	"""

	template = "personEdit.html"
	return render(request, template, context)

def addUser(request):
	context = dict()
	current_user = request.user
	form = PersonForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			data2 = form.save(commit=False)
			print("form valid")
			data2 = Personal()
			data2.user = current_user
			data2.name = form.cleaned_data['name']
			data2.surname = form.cleaned_data['surname']
			data2.email = form.cleaned_data['email']
			data2.abouts = form.cleaned_data['abouts']
			data2.phone = form.cleaned_data['phone']
			data2.f_account = form.cleaned_data['f_account']
			data2.i_account = form.cleaned_data['i_account']
			data2.t_account = form.cleaned_data['t_account']


			try:
				q1 = Personal.objects.get(user_id=current_user.id)
				print("addUser try", q1)
			except:
				q1 = None
				print("addUser except çalıştı")
			if q1 != None:
				messages.success(request, ' This book comments is already added')
			else:
				data2.user_id = current_user.id
				data2.save()
				messages.success(request, ' Thank You')
		return HttpResponseRedirect("/about")

	template = 'about.html'
	return render(request, template, context)
