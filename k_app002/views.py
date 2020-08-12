from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from k_app002.form import HelloForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'Hello',
            # 'message': 'your data:',
            'form': HelloForm(),
            'result': None
        }

    def get(self, request):
        return render(request, 'k_app002/index.html', self.params)

    def post(self, request):
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
        ch = request.POST.getlist('choice')
        result = '<ol class="list-group"><b>selected:</b>'
        for item in ch:
            result += '<li class="list-group-item">' + item + '</li>'
        result += '</ol>'
        self.params['result'] = result
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
