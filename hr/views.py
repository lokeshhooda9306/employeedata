from django.shortcuts import render, HttpResponseRedirect
from .modelform import hoodareg
from .models import hooda

# Create your views here.
def index(request):
    fm = hoodareg()
    showdata = hooda.objects.all()
    if request.method == "POST":
        fm = hoodareg(request.POST)
        
        if fm.is_valid():
            name = fm.cleaned_data['name']
            rollno = fm.cleaned_data['rollno']
            mobile_no = fm.cleaned_data['mobile_no']
            email = fm.cleaned_data['email']
            reg = hooda(name=name,rollno=rollno,mobile_no=mobile_no,email=email)
            reg.save()
    return render(request, "index.html", {'form':fm, 'dt':showdata})

def update(request,my_id):
    showdb = hooda.objects.get(pk=my_id)
    form = hoodareg(request.POST, instance=showdb)

    if form.is_valid():
        showdb = form.save()

        return HttpResponseRedirect('/index/')





