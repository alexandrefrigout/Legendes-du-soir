from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from lescontes.models import Ibook
from django.shortcuts import render, render_to_response

def makeAddress(titre, idApple):
	baseLink = 'itms://itunes.apple.com/fr/book/'
	formatedTitle = titre.lower().replace(" ", "-")
	return "".join([baseLink, formatedTitle, '/id', idApple])
	#print formatedTitle

def index(request, lang=None):
	if not lang:
		all_ibooks = Ibook.objects.order_by('id')[:]
	else:
		print lang
		all_ibooks = Ibook.objects.filter(langue=lang.upper())

	paginator = Paginator(all_ibooks, 5)
	page = request.GET.get('page')
	try:
		ibooks = paginator.page(page)
	except PageNotAnInteger:
		ibooks  = paginator.page(1)
	except EmptyPage:
		ibooks = paginator.page(paginator.num_pages)
	for i in ibooks:
		i.idapple = makeAddress(i.titre, i.idapple)
	#print request.META['HTTP_USER_AGENT']
	return render(request, 'lescontes/index.html', {'tous_les_contes':ibooks})

class IbookForm(forms.ModelForm):
	class Meta:
		model = Ibook

@login_required
def adminHome(request):
	all_ibooks = Ibook.objects.order_by('id')[:]
	return render(request, 'lescontes/adminhome.html', {'tous_les_contes':all_ibooks})


@login_required
def ajouterIbook(request):
	if request.method == 'POST':
		form = IbookForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/adminhome')
		else:
			return HttpResponseRedirect('/addibook')
	else:
		form = IbookForm()
		return render(request, "lescontes/addibook.html", {'form': form})

@login_required
def deletebook(request, title):
	todel = Ibook.objects.filter(id=title)
	todel.delete()
	all_ibooks = Ibook.objects.order_by('id')[:]
	return render(request, 'lescontes/adminhome.html', {'tous_les_contes':all_ibooks})

@login_required
def editibook(request, title):
	if not title:
		tomodif = Ibook(id=request.user)
	else:
		tomodif = Ibook.objects.get(id=title)
	if request.method == 'POST':
		form = IbookForm(request.POST, instance=tomodif)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/adminhome')
	else:
		form = IbookForm(instance=tomodif)
	return render(request, "lescontes/editibook.html", {'form': form})
	

@login_required
def recherche(request):
	error = False
	if 'chaine' in request.GET:
		chaine = request.GET['chaine']
		if not chaine:
			error = True
		else:
			leIbook = Ibook.objects.filter(titre__icontains=chaine)
			return render(request, 'lescontes/adminhome.html', {'tous_les_contes':leIbook})
	return HttpResponseRedirect('/adminhome')


@login_required
def logoutadmin(request):
	logout(request)
	return HttpResponseRedirect('/')
