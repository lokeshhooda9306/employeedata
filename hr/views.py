from django.shortcuts import render,HttpResponseRedirect
from .modelform import hoodareg
from .models import hooda
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
class MyView(View):
    form_class = hoodareg
    template_name="index.html"

    def get_context_data(self, **kwargs):
        showdata = hooda.objects.all()
        fm = hoodareg()
        context = {"dt":showdata, "fm":fm}
        return context

    def get(self, request):
        showdata = hooda.objects.all()
        fm = hoodareg()
        form = {"dt":showdata, "fm":fm}
        return render(request, "index.html", form)


    def post(self, request):
        showdata = hooda.objects.all()
        if self.request.POST:
            fm = hoodareg(self.request.POST)
        
        else:
            fm = hoodareg()
        
        if fm.is_valid():
            name = fm.cleaned_data['name']
            rollno = fm.cleaned_data['rollno']
            mobile_no = fm.cleaned_data['mobile_no']
            email = fm.cleaned_data['email']
            reg = hooda(name=name,rollno=rollno,mobile_no=mobile_no,email=email)
            reg.save()
            print("object created succesfully")
        
            return HttpResponseRedirect("/index")

        if 'update' in request.POST:
            print("hello in the terminal")
        
        return render(request, "index.html", {'form':fm,"dt":showdata})



class MyViewUpdate(UpdateView):
    model = hooda
    template_name = 'update.html'
    fields = '__all__'
    success_url='/index/'
    
    def success(request):
        return render(request,'index.html')

class MyViewDelete(DeleteView):
    model = hooda
    template_name = 'delete.html'
    success_url='/index/'
    
    def success(request):
        return render(request,'index.html')
        






