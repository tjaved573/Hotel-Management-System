from django import forms
from guest.models import Hotel


class ReservationForm(forms.Form):
    check_in_date = forms.DateField(input_formats=['%Y/%m/%d'])
    check_out_date = forms.DateField(input_formats=['%Y/%m/%d'])
    rooms = forms.ChoiceField(choices=[None])
    payment_type = forms.ChoiceField(choices=[('credit','credit'),('cash','cash')])
    Credit_card_number = forms.CharField(max_length=20)

    def __init__(self, selected_room_bundle):
        super(ReservationForm, self).__init__()
        self.fields['rooms'].choices = selected_room_bundle



