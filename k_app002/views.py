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
from django.db.models import Count,Sum,Avg,Min,Max
from .forms import CheckForm
from django.core.paginator import Paginator
from .models import Friend, Message
from .forms import FriendForm, MessageForm




class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend


def index(request, num=1):   
    data = Friend.objects.all()
    page = Paginator(data, 3)
    # re1 = Friend.objects.aggregate(Count('age'))
    # re2 = Friend.objects.aggregate(Sum('age'))
    # re3 = Friend.objects.aggregate(Avg('age'))
    # re4 = Friend.objects.aggregate(Min('age'))
    # re5 = Friend.objects.aggregate(Max('age'))
    # msg = 'count:' + str(re1['age__count']) + '<br>Sum:' + str(re2['age__sum']) + '<br>Average:' + str(re3['age__avg']) + '<br>Min:' + str(re4['age__min']) + '<br>Max:' + str(re5['age__max'])
    params = {
        'title': 'Hello',
        'message':'',
        'data': page.get_page(num),
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
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from k_app002_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
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

def check(request):
    params = {
        'title': 'Hello',
        'message': 'check validation.',
        'form': FriendForm(),
    }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'k_app002/check.html', params)


def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'k_app002/message.html', params)





