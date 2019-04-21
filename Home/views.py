from django.shortcuts import render
from .models import *
from .forms import UpSP_Form
from django.shortcuts import redirect
# Create your views here.

def Home(request):
    ListSP = Sanpham.objects.all()
    return render(request, 'Home/Home.html', {'ListSP': ListSP})

def Up_sp(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UpSP_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('up')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpSP_Form()

    return render(request, 'UpLoad/Upload_SP.html', {'form': form})
