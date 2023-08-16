from django.shortcuts import render,HttpResponse,redirect
from .models import Details,Project
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
import uuid
# from .utils  import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,'loginpage.html')
def signup(request):
    return render(request,'signup.html')
def login_after_signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first-name')
        last_name=request.POST.get('last-name')
        emailid=request.POST.get('emailid')
        mobile_number=request.POST.get('mobile-number')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm-password')
        gender=request.POST.get('gender')
        if confirm_password==password:

            if ((len(Details.objects.filter(mailId=emailid)) == 0) and
                (len(Details.objects.filter(phoneNumber=mobile_number))==0)):

                username=emailid.split("@")[0]
                # profile_obj=Profile(user=User(emailid,password=password),
                #                     email_token=str(uuid.uuid4()))


                obj = Details(firstNname=first_name, lastName=last_name, mailId=emailid, phoneNumber=mobile_number,
                              password=password, gender=gender)
                obj.save()
                user = User.objects.create_user(username=username, email=emailid, password=password)
                # send_email_token(email=emailid, token=profile_obj.email_token)

                return render(request,'loginpage.html')
            else:
                context={
                    'message': "Email already exists"
                }
                return render(request,'signup.html',context)
        else:
            context = {
                'message': "confirm password field must be same as password"
            }
            return render(request,'signup.html',context)
    else:
        return redirect('/')

def dashboard(request):
    if request.method=='POST':
        emailid=request.POST.get('email')
        password=request.POST.get('password')
        user_name=emailid.split("@")[0]
        user=authenticate(username=user_name,password=password)
        if user is not None:
            auth_login(request, user)
            context={
                'username':user_name,
            }
            return render(request,'user_dashboard.html',context=context)
        else:

            return redirect('/login_failed')
    return redirect('/')

def logout_account(request):
    logout(request)
    return redirect('/')
def login_failed(request):
    context = {
        'message': "Entered Wrong Credentials"
    }

    return render(request, 'loginpage.html', context)

def createProject(request):
    return render(request,'main.html')

def result(request):
    user=request.user
    username=user.username
    if request.method=="POST":
        project_name=request.POST.get('project-name')
        dataset=request.FILES['train_data']
        filetype=request.POST.get('filetype')
        obj=Project(username=username,projectname=project_name,dataset=dataset)
        obj.save()
        obj2=Project.objects.filter(projectname=project_name)
        context={
            'url':obj2
        }
        return render(request,'test.html',context=context)
    else:
        return redirect('/create_new_project')



# def create_user(request):


# def verify(request,token):
#     try:
#         obj=Profile.objects.get(email_token=token)
#         obj.is_verified=True
#         obj.save()
#
#     except Exception as e:
#         return HttpResponse("token is invalid")

