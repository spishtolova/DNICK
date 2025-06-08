from django.shortcuts import render, redirect
from .models import Candy, Supplier
from .forms import CandyForm

# Create your views here.

def home(request):
    candies = Candy.objects.all()
    return render(request, 'main.html', context = {'candies': candies})

def add_candy(request):
    if request.method == 'POST':
        form = CandyForm(request.POST, request.FILES)
        if form.is_valid():
            candy = form.save(commit=False)
            candy.supplier = Supplier.objects.filter(user=request.user).first()
            candy.save()

        return redirect('home')

    form = CandyForm()
    return render(request, 'add_candy.html', context={'form': form})