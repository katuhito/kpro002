from django import forms
from.models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
        

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
    
