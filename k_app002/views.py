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




class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

# def __new_str__(self):
#     result = ''
#     for item in self:
#         result += '<tr>'
#         for k in item:
#             result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
#         result += '</tr>'
#     return result

# QuerySet.__str__ = __new_str__

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
    # if (request.method == 'POST'):
    #     name = request.POST['name']
    #     mail = request.POST['mail']
    #     gender = 'gender' in request.POST
    #     age = int(request.POST['age'])
    #     birth = request.POST['birthday']
    #     friend = Friend(name=name, mail=mail, gender=gender, age=age, birthday=birth)

    #     friend.save()
    #     return redirect(to='/k_app002')
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








# def index(request):
#     params = {
#         'title': 'Hello',
#         'message': 'all friends',
#         'form': HelloForm(),
#         'data': [],
#     }
#     if (request.method == 'POST'):
#         num = request.POST['id']
#         item = Friend.objects.get(id=num)
#         params['data'] = [item]
#         params['form'] = HelloForm(request.POST)
#     else:
#         params['data'] = Friend.objects.all()
#     return render(request, 'k_app002/index.html', params)



    

# def index(request):
#     data = Friend.objects.all()
#     params = {
#         'title': 'Hello',
#         'message': 'all friends',
#         'data': data,
#     }
#     return render(request, 'k_app002/index.html', params)


# class HelloView(TemplateView):

#     def __init__(self):
#         self.params = {
#             'title': 'Hello',
#             # 'message': 'your data:',
#             'form': HelloForm(),
#             'result': None
#         }

#     def get(self, request):
#         return render(request, 'k_app002/index.html', self.params)

    # def post(self, request):
        # msg = 'あなたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')<b>さんです。<br>メールアドレスは　<b>' + request.POST['mail'] + '</b>ですね。'
        # self.params['message'] = msg

        # if('check' in request.POST):
        #     self.params['result'] = 'Checked!!'
        # else:
        #     self.params['result'] = 'not checked...'
        # self.params['form'] = HelloForm(request.POST)
        # return render(request, 'k_app002/index.html', self.params)

    # 3択チェックボックス
        # chk = request.POST['check']
        # self.params['result'] = 'you selected: "' + chk + '".'
        # self.params['form'] = HelloForm(request.POST)
        # return render(request, 'k_app002/index.html', self.params)

    # プルダウンメニュー
        # ch = request.POST['choice']
        # self.params['result'] = 'selected: "' + ch + '".'
        # self.params['form'] = HelloForm(request.POST)
        # return render(request, 'k_app002/index.html', self.params)

    # マルチプルリスト
        # ch = request.POST.getlist('choice')
        # self.params['result'] = 'selected: ' + str(ch) + '.'
        # self.params['form'] = HelloForm(request.POST)
        # return render(request, 'k_app002/index.html', self.params)

    # リストの値を利用
        # ch = request.POST.getlist('choice')
        # result = '<ol class="list-group"><b>selected:</b>'
        # for item in ch:
        #     result += '<li class="list-group-item">' + item + '</li>'
        # result += '</ol>'
        # self.params['result'] = result
        # self.params['form'] = HelloForm(request.POST)
        # return render(request, 'k_app002/index.html', self.params)






# def index(request):
#     params = {
#         'title': 'Hello',
#         'message': 'your data:',
#         'form': HelloForm()
#     }
#     if (request.method == 'POST'):
#         params['message'] = '名前：' + request.POST['name'] + '<br>メール：' + request.POST['mail'] + '<br>年齢：' + request.POST['age']

#         params['form'] = HelloForm(request.POST)

#     return render(request, 'k_app002/index.html', params)
