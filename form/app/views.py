from django.http import *
from django.shortcuts import render
from .form import *
from .models import *


# Create your views here.
def vform(request):
    if request.method == "POST":
        temp = form(request.POST)
        if temp.is_valid():
            temp.save()
            return HttpResponseRedirect('/')
    else:
        temp=form()
        return render(request, 'form.html', {'form':temp})


def data(request):
    sdata = student.objects.all()

    stud = {
        "a": sdata
    }
    return render(request, 'data.html', stud)
