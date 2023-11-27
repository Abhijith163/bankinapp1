# mybankingapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import District, UserProfile,Branch

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
     

    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    district = forms.ChoiceField(choices=[])

    account_type_choices = [('savings', 'Savings Account'), ('current', 'Current Account')]
    materials_provide_choices = [('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')]

    account_type = forms.ChoiceField(choices=account_type_choices)
    materials_provide = forms.MultipleChoiceField(
        choices=materials_provide_choices,
        widget=forms.CheckboxSelectMultiple
    )
    
    class UserProfileForm(forms.ModelForm):
        dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
        district = forms.ChoiceField(choices=[])
        branch = forms.ModelChoiceField(queryset=Branch.objects.all())

    class Meta:
        model = UserProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['district'].choices = [('', 'Select District')] + [(district.id, district.name) for district in District.objects.all()]

        

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age

