from django.shortcuts import render, redirect
from crud.forms import PatrimoniosForm
from crud.models import Patrimonios
from django.core.paginator import Paginator 

# Create your views here.


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Patrimonios.objects.filter(MODELO__icontains=search)
    else:
        data['db'] = Patrimonios.objects.all()

    #all = Patrimonios.objects.all()
    #paginator = Paginator(all, 5)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = PatrimoniosForm()
    return render(request, 'form.html', data)

def create(request):
    form = PatrimoniosForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Patrimonios.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Patrimonios.objects.get(pk=pk)
    data['form'] = PatrimoniosForm(instance=data['db']) 
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Patrimonios.objects.get(pk=pk)
    form = PatrimoniosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
           form.save()
    return redirect('home')

def delete(request, pk):
    db = Patrimonios.objects.get(pk=pk)
    db.delete()
    return redirect('home')