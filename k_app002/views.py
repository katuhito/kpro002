from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from k_app002.form import HelloForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data:',
            'form': HelloForm()   
        }

    def get(self, request):
        return render(request, 'k_app002/index.html', self.params)

    def post(self, request):
        msg = 'あなたは、<b>' + request.POST['name'] + '(' + request.POST['age'] + ')<b>さんです。<br>メールアドレスは　<b>' + request.POST['mail'] + '</b>ですね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'k_app002/index.html', self.params)
        


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



    






