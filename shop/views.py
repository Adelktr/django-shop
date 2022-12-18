from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Articles
from .forms import ArticlesForm

# Create your views here.

def index(request):
    context = {}
 
    # add the dictionary during initialization
    context["dataset"] = Articles.objects.all()
         
    return render(request, "shop/index.html", context)


def create(request):

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:index')
            
    else:
        form = ArticlesForm()
        
    context = {
        'form': form
    }
    return render(request, 'shop/create.html', context)

def show(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
 
    # add the dictionary during initialization
    context["data"] = Articles.objects.get(id = id)
         
    return render(request, "shop/show.html", context)

def update(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Articles, id = id)
 
    # pass the object as instance in form
    form = ArticlesForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/shop/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "shop/update.html", context)

def delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Articles, id = id)
 
    obj.delete()

    return HttpResponseRedirect("/shop/")

