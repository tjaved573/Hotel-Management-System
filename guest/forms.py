from django import forms
from guest.models import Hotel


class HotelForm(forms.Form):
    hotel = forms.ChoiceField(choices=[None])
    check_in_date = forms.DateField(input_formats=['%Y/%m/%d'])
    check_out_date = forms.DateField(input_formats=['%Y/%m/%d'])
    rooms = forms.ChoiceField(choices=[(None, 'Please select a hotel')]) # TODO: get rooms associated with hotel
    payment_type = forms.ChoiceField(choices=[('credit','credit'),('cash','cash')])
    Credit_card_number = forms.CharField(max_length=20)

    def __init__(self, hotel_objs):
        super(HotelForm, self).__init__()
        self.fields['hotel'].choices = [(h, h.location) for h in hotel_objs]



