from django import forms

from .models import Show
from django.core.validators import MaxValueValidator, MinValueValidator


class ShowForm(forms.ModelForm):
    Title=forms.CharField(max_length=100,label='Title')
    Network = forms.CharField(max_length=30, label='Network')
    Release_date = forms.DateField(label='Release_date')
    Description = forms.TextInput(attrs={ 'required': 'true' })
    class Meta:
        model = Show
        fields = ('Title', 'Network','Release_date','Description')
    
    # To add styles
    def __init__(self, *args, **kwargs):
        super(ShowForm, self).__init__(*args, **kwargs)
        self.fields['Title'].widget.attrs.update({'class' : 'form-control'}),
        self.fields['Network'].widget.attrs.update({'class' : 'form-control'}),
        self.fields['Release_date'].widget.attrs.update({'class' : 'form-control'}),
        self.fields['Description'].widget.attrs.update({'class' : 'form-control'})

     
    # Form Validations
    def clean(self):
        # data from the form is fetched using super function
        super(ShowForm, self).clean()

        title = self.cleaned_data.get('Title')
        Network = self.cleaned_data.get('Network')
        Description = self.cleaned_data.get('Description')

        if len(title) < 2:
            self._errors['Title'] = self.error_class([
                'Minimum 2 characters required'])
        if len(Network) < 3:
            self._errors['Network'] = self.error_class([
                'Network Should Contain a minimum of 3 characters'])
        if Description:
            if len(Description) < 10:
                self._errors['Description'] = self.error_class([
                    'Description Should Contain a minimum of 10 characters'])
        # return any errors if found
        return self.cleaned_data

