from django import forms
from .models import Friend
from .models import Friend, Message

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'birthday': forms.DateInput(attrs={'class':'form-control'}),
        }



class HelloForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='Gender', required=False, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateField(label='Birth', widget=forms.DateInput(attrs={'class':'form-control'}))
    # id = forms.IntegerField(label='ID')
    
    # name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
    # mail = forms.CharField(label='mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    # age = forms.IntegerField(label='age', widget=forms.NumberInput(attrs={'class':'form-control'}))
    # check = forms.BooleanField(label='Checkbox', required=False)
    # check = forms.NullBooleanField(label='Check')

    # data = [
    #     ('one', 'item 1'),
    #     ('two', 'item 2'),
    #     ('three', 'item 3'),
    #     ('four', 'item 4'),
    #     ('five', 'item 5')
    # ]

    # 選択リスト
    # choice = forms.ChoiceField(label='radio', choices=data, widget=forms.Select(attrs={'size': 5}))

    # 複数項目の選択
    # choice = forms.MultipleChoiceField(label='radio', choices=data, widget=forms.SelectMultiple(attrs={'size': 6}))
    
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class CheckForm(forms.Form):
    # empty = forms.CharField(label='Empty', empty_value=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # min = forms.CharField(label='Min', min_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # max = forms.CharField(label='Max', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

# 数値を扱う
    # required = forms.IntegerField(label='Required', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # min = forms.IntegerField(label='Min', min_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # max = forms.IntegerField(label='Max', max_value=1000, widget=forms.NumberInput(attrs={'class': 'form-control'}))

# 日時を扱う
    # date = forms.DateField(label='Date', input_formats=['%d'], widget=forms.DateInput(attrs={'class': 'form-control'}))
    # time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'class': 'form-control'}))
    # datetime = forms.DateTimeField(label='DateTime', widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

# 「NO」でエラーを発生させる
    str = forms.CharField(label='String', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('you input "NO"!')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':2}),
            'friend': forms.Select(attrs={'class':'form-control form-control-sm'}),
        }
        

        




