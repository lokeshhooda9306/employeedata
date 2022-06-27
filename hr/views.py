from django.shortcuts import render,HttpResponseRedirect
from .modelform import hoodareg
from .models import hooda
from django.views import View


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
        template_name="index.html"
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
            return HttpResponseRedirect("/index")
        
        return render(request, "index.html", {'form':fm,"dt":showdata})



        
class delete_view(View):
    def get(self, request, **kwargs):
        id = kwargs['my_id']
        data_del = hooda.objects.get(pk=id)
        data_del.delete()
        return HttpResponseRedirect('/index')
        


class update_view(View):
    def get(self, request,**kwargs):
        id = kwargs['my_id']
        
        data_show = hooda.objects.get(pk=id)
        data_form = hoodareg( instance= data_show)
        data_show.save()
        return render(request, "update.html", {'form':data_form,'data':data_show})

    def post(self ,request, **kwargs):
        id =kwargs['my_id']
        data_show = hooda.objects.get(pk=id)
        if self.request.POST:
            data_form = hoodareg(self.request.POST, instance= data_show)
        if data_form.is_valid():
            data_show.save()
            return HttpResponseRedirect('/index')
        
        return render(request, "update.html", {'form':data_form,'data':data_show})




    # return render(request, "update.html", {'form':data_form,'data':data_show})
        



# def delete(request,my_id):
#     showdb = hooda.objects.get(id=my_id).delete()

#     return HttpResponseRedirect('/index')

# def update(request,my_id):
#     showdb = hooda.objects.get(pk=my_id)
#     print(showdb.name)
#     form = hoodareg(request.POST, instance=showdb)

#     if form.is_valid():
#         showdb= form.save(commit= False)
#         showdb.save()

#         return HttpResponseRedirect('/index')

#     else:
#         return render (request,'update.html',{"form": form,"showdb":showdb})
        
        

    
    






