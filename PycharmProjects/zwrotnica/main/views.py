from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from main.models import Donation, Institution, User


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

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user = User.objects.create_user(first_name=name,
                                            last_name=surname,
                                            email=email,
                                            password=password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Wprowadzone hasła nie są identyczne'})
