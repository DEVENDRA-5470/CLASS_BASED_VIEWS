from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import *
from main.models import *
# Create your views here.
class homeview(View):
    def get(self,request):
        data=Student.objects.all()
        con={'data':data}

        return render(request,'home.html',con)
    
class aboutview(View):
    def get(self,request):
        return render(request,'about.html')

class sign_up(View):
    def get(self,request):
        form=myform()
        context={'form':form}
        return render(request,'sign_up.html',context)
    
    def post(self,request):
        form=myform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done")
        else:
            context={'form':form}
            return render(request,'sign_up.html',context)

class register(View):
    template_name = '' 

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Extract data from the request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        country = request.POST.get('countries')
        technologies =request.POST.getlist('technology')
        identification = request.POST.get('list-radio')
        date = request.POST.get('date')
        time = request.POST.get('time')
        area = request.POST.get('area')
        city = request.POST.get('city')
        state = request.POST.get('state')
        post_code = request.POST.get('post-code')

        # Create a new Customer instance and save it to the database
        customer_instance = Customer.objects.create(
            name=name,
            phone=phone,
            email=email,
            country=country,
            technologies=technologies,
            identification=identification,
            date=date,
            time=time,
            area=area,
            city=city,
            state=state,
            post_code=post_code
        )
        customer_instance.save()

        # You can customize the response based on your needs
        return JsonResponse({'message': 'Data saved successfully'})
    



# crud operation

class create_view(View):
    def get(self,request):
        form = Student_form()
        context={"form":form}
        return render(request,"addstudent.html",context)
    
    def post(self,request):
        form =Student_form(data=request.POST)
        if form.is_valid():
            student=form.save()
            return redirect('home')
        
# Delete View

class delete_view(View):
    def get(self, request, id):
        student = get_object_or_404(Student, pk=id)
        student.delete()
        return HttpResponseRedirect('/')

# Update View
class update_view(View):
    def get(self, request, id):
        student = get_object_or_404(Student,pk=id)
        form = Student_form(instance=student)
        context={"form":form}
        return render(request,'updatestudent.html',context)
    
    def post(self,request,id):
        student=Student.objects.get(pk=id)
        form=Student_form(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("home")

