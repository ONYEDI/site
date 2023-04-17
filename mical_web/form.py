from django import forms

class WorkForm(forms.Form):
    app = forms.CheckboxInput()
    data = forms.CheckboxInput()
    graphic = forms.CheckboxInput()
    web = forms.CheckboxInput()
    machine = forms.CheckboxInput()
    name = forms.CharField(label='name',max_length=50)
    email = forms.EmailField(label='email',max_length=50)