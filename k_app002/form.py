from django import forms

class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')
    
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
    
