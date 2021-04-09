from main.models import Donation
import django.forms as forms


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        exclude = ('user', 'categories',)
