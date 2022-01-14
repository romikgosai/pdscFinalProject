from django.shortcuts import redirect, render

from pages.models import Contact, Course
from pages.forms import MyForm


# Create your views here.

def home(request):
    courses = Course.objects.all()
    form = MyForm()
    context = {
        "courses": courses,
        "form" : form,
    }
    return render(request,'index.html',context)

def add(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')