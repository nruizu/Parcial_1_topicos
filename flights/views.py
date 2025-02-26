from django.views.generic import TemplateView, View, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms 
from .models import Flight
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'type', 'price']

class Register(View):
    template_name = 'register.html'

    def get(self, request):
        form = FlightForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})


