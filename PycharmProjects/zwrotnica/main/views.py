
from django.shortcuts import render
from django.views import View

from main.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags_total = 0
        for d in donations:
            bags_total += d.quantity
        donated_institutions = Institution.objects.filter(donation__gt=0).count()
        foundations = Institution.objects.filter(type='F')
        ngos = Institution.objects.filter(type='OP')
        fundraisers = Institution.objects.filter(type='ZL')
        ctx = {
            'bags_total': bags_total,
            'donated_institutions': donated_institutions,
            'foundations': foundations,
            'ngos': ngos,
            'fundraisers': fundraisers,
        }
        return render(request, 'index.html', ctx)

class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
