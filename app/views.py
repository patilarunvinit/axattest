
from django.shortcuts import render,redirect
from .models import data,reg

from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User






# Create your views here.
@csrf_exempt
def registration(request):
    if request.method =='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile_no = request.POST.get("mobile_no")
        user = request.POST.get("user")
        option = request.POST.get("option")

        try:
            a = reg.objects.create(email=email, mobile_no=mobile_no, option=option)
            if a:
                print(name, email, password, mobile_no, user)
                out = User.objects.create_user(username=user, password=password, email=email, first_name=name)
                out.save()
                mas = {
                    'mass': False,
                }
                return render(request, "reg.html", mas)

            else:
                mas = {
                    'mass': True,
                }
                return render(request, "reg.html", mas)
        except:
            mas={
                'mass':True
            }
            return render(request, "reg.html",mas)
    return render(request, "reg.html")








@csrf_exempt
@permission_classes((AllowAny,))
def loginmain(request):
   if request.method == "POST":
       email = request.POST.get('email')
       password = request.POST.get('password')
       option = request.POST.get('option')
       if email=="" or password =="":
           return redirect('http://127.0.0.1:8000/')

       user = authenticate(username=email, password=password,last_name=option)
       print(user)
       #print(user.username,user.password,user.first_name,user)
       if not user:
           return redirect('http://127.0.0.1:8000/')

       else:
           login(request,user)
           request.session['email'] = user.email
           request.session['option'] = user.first_name
           token, _ = Token.objects.get_or_create(user=user)

           if user.first_name =="admin" :
              return redirect('http://127.0.0.1:8000/ad/')

           elif user.first_name =="teacher" :
              return redirect('http://127.0.0.1:8000/teacher/')

           elif user.first_name =="student" :
              return redirect('http://127.0.0.1:8000/student/')
      
   return render(request, "login.html")




def admin(request):
    if request.method == 'POST':
        image=request.FILES['image']
        email = request.session['email']
        option = request.session['option']
        data.objects.create(image=image,email=email,option=option)
        return render(request, "admin.html")

    elif request.method == 'GET':
        email = request.session['email']
        output = data.objects.all().values()
        context = {
            'mymembers': output,
            'email':email
        }
        return render(request, "admin.html",context)




def teacher(request):
    if request.method == 'POST':
        image = request.FILES['image']
        email = request.session['email']
        option = request.session['option']
        data.objects.create(image=image, email=email, option=option)
        return render(request, "teacher.html")

    elif request.method == 'GET':
        email = request.session['email']
        print(email)
        option = request.session['option']
        selfdata = data.objects.all().filter(email=email,option=option).values()
        studentdata = data.objects.all().filter(option='student').values()
        context = {
            'mymembers': selfdata,
            'test123':studentdata,
            'email': email
        }
        return render(request, "teacher.html", context)





def student(request):
    if request.method == 'POST':
        image = request.FILES['image']
        email = request.session['email']
        option = request.session['option']
        data.objects.create(image=image, email=email, option=option)
        return render(request, "student.html")

    elif request.method == 'GET':
        email = request.session['email']
        option = request.session['option']
        selfdata = data.objects.all().filter(email=email,option=option).values()
        context = {
            'mymembers': selfdata,
            'email': email
        }
        #print(context['mymembers'])
        return render(request, "student.html", context)