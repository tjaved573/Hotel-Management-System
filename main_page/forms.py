from django import forms

class ReservationForm(forms.Form):
    check_in_date       = forms.DateField()
    check_out_date      = forms.DateField()
    guest_id            = forms.IntegerField()
    payment_type        = forms.CharField(max_length=10)
    credit_card_number  = forms.CharField(max_length=20)

class FeatureForm(forms.Form):
    feature_id      = forms.IntegerField()
    feature         = forms.CharField(max_length=20)
    price           = forms.DecimalField(max_digits=9, decimal_places=2)
    description     = forms.CharField(max_length=255)
