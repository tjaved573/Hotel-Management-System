from django import forms
from guest.models import Hotel
import datetime

# adding new guest for our application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReservationForm(forms.Form):
    check_in_date = forms.DateField(initial=datetime.date.today)
    check_out_date = forms.DateField(initial=datetime.date.today)
    room = forms.ChoiceField(choices=[('None','sdf')])
    payment_type = forms.ChoiceField(choices=[('credit','credit'),('cash','cash')])
    credit_card_number = forms.CharField(max_length=20, required=False)


    def __init__(self,selected_room_bundle,*args,**kwargs):
        super(ReservationForm,self).__init__(*args,**kwargs)
        self.fields['room'].choices = selected_room_bundle


# new form for registration of user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
