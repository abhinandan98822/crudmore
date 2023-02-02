from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Register
from django.contrib import messages


# Create your views here.
def RegisterView(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        age=request.POST.get('age')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        if password!=confirm_password:
            messages.error(request,'password did not match')
            return redirect('register')
        else:    
            mobile=request.POST.get('mobile') 
            gender=request.POST.get('gender')   
            print(gender,'gender')
            data=Register(firstname=firstname,lastname=lastname,age=age,email=email,password=password,mobile=mobile,gender=gender)
            data.save()
            messages.success(request,'data saved successfully')
    return render(request,'register.html')

def Table(request):
    data=Register.objects.all().order_by('firstname').values()
    context={"data":data}
    return render(request,'table.html',context)   

def Edit(request,id):
    M="Male"
    F="Female"
    O="Others"
    data=Register.objects.get(id=id)
    fieldobject=Register._meta.get_field('gender')
    main_value=fieldobject.value_from_object(data)
    if main_value=="Male":
        context={'data':data,"male":M}
    elif main_value=="Female":
        context={'data':data,"female":F}
    else:
        context={'data':data,"others":O}    
    return render(request,'edit.html',context)

def Delete(request,id):
    data=Register.objects.get(id=id).delete()
    messages.success(request,'data deleted..')
    return redirect('table')

def Update(request,id):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        age=request.POST.get('age')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile') 
        gender=request.POST.get('gender')  
        data=Register.objects.get(id=id)
        data.firstname=firstname
        data.lastname=lastname
        data.age=age
        data.email=email
        data.mobile=mobile
        data.gender=gender
        messages.success(request,'data has been updated successfully.')
        data.save()
    return redirect('table')

def Search(request):
    if request.method=="GET":
        search=request.GET.get('search')
        print(search)
        try:
            status=Register.objects.filter(firstname__icontains=search)
            print(status)
            return render(request,"table.html",{"result":status})
        except:
            return render(request,"table.html",{"result":status})
    # else:
    return redirect('table')
    