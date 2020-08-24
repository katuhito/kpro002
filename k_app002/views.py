from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import TemplateView
# from .forms import HelloForm
from .forms import FriendForm
from .models import Friend
from django.shortcuts import redirect
# from django.db.models import QuerySet
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from django.db.models import Q



class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend


def index(request):   
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'k_app002/index.html', params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/k_app002')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
   
    return render(request, 'k_app002/create.html', params)
    
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/k_app002')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'k_app002/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/k_app002')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'k_app002/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        mag = 'serch result:'
        form = FindForm(request.POST)
        find = request.POST['find']
        list = find.split()
        data = Friend.objects.filter(name__in=list) 
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'k_app002/find.html', params)


