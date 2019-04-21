from django.forms import ModelForm
from django.db import models
from .models import Sanpham

# Create the form class.
class UpSP_Form(ModelForm):
    class Meta:
        model = Sanpham
        fields = '__all__'
