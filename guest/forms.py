from django import forms
from guest.models import Hotel
import datetime

# adding new guest for our application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.validators import EMPTY_VALUES


class ReservationForm(forms.Form):
    check_in_date = forms.DateField(initial=datetime.date.today)
    check_out_date = forms.DateField(initial=datetime.date.today)
    room = forms.ChoiceField(choices=[('None','sdf')])
    payment_type = forms.ChoiceField(choices=[('credit','credit'),('cash','cash')])
    credit_card_number = forms.CharField(max_length=20, required=False)


    def __init__(self,selected_room_bundle,*args,**kwargs):
        super(ReservationForm,self).__init__(*args,**kwargs)
        self.fields['room'].choices = selected_room_bundle
    
    def clean(self):
        credit_card = self.cleaned_data.get('payment_type') == 'credit'
        if credit_card:
            credit_card_number = self.cleaned_data.get('credit_card_number', None)
            if credit_card_number in EMPTY_VALUES:
                self._errors['credit_card_number'] = self.error_class(['Credit card number required here'])
        return self.cleaned_data


# new form for registration of user
class CreateUserForm(UserCreationForm):
    firstname = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    lastname = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.', widget=(forms.TextInput(attrs={'class': 'form-control'})))

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username', 'email', 'password1',)

    def __init__ (self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        self.fields.pop ('password2')


class FilterForm(forms.Form):
    lower_price = forms.DecimalField(max_digits=5, decimal_places=2, help_text='Required: Lower Search Price')

    # class Meta:
    #     model = User
    #     fields = ('lower_price',)

    def __init__ (self, *args, **kwargs):
        super(FilterForm,self).__init__(*args, **kwargs)

