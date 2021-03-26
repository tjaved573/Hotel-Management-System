from django import forms

class ReservationForm(forms.Form):
    check_in_date       = forms.DateField()
    check_out_date      = forms.DateField()
    guest_id            = forms.IntegerField()
    payment_type        = forms.CharField(max_length=10)
    credit_card_number  = forms.CharField(max_length=20)
