from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login, logout
# from django.core.mail import send_mail, EmailMessage
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.utils.encoding import force_str
from . tokens import generate_token
# from publication import settings
from authentication.services import get_faculty_papers_by_email, get_papers_by_author_id
from django.shortcuts import render, redirect
# from .forms import UserCreationForm
# from rest_framework.views import APIView
# from rest_framework.response import Response
# Create your views here.

def home(request):
    return render(request, 'index.html')

def signup(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        '''
        Alternate method to get values filled in form
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        '''
            
        if pass1==pass2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists!, Please try another username.')
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email already registered!')
                return redirect('signup')
            elif len(username) > 10:
                messages.error(request,"Username must be under 10 characters!")
                return redirect(request,'signup')
            elif not username.isalnum():
                messages.info(request,"Username must contain only letters and number.")
                return redirect('signup')
            else:
                newUser  = User.objects.create_user(username,email,pass1,fname,lname)
                newUser.first_name = fname
                # newUser.is_active = False
                newUser.save()
            
                messages.success(request,"Your account has been successfully created.")
                return render(request,'sigin.html' )
        
            # #welcome message via email
            # subject = "Welcome to USPS - Login"
            # message = "Hello" + newUser.first_name + "!! \n" + "Welcome to USPS \n Thank You for visiting USPS \n We have sent you a confirmation email, please confirm your email address in order to activate your account \n\n Thank You \n Regards \n Admin"
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [newUser.email]
            # send_mail(subject,message,from_email,to_list,fail_silently=True)
            
            # #Email address confirmation email
            
            # current_site = get_current_site(request)
            # email_subject = "Confirm your email @USPS-Login"
            # message2 = render_to_string('email_confirmation.html', {
            #     'name': newUser.first_name,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(newUser.pk)),
            #     'token':generate_token.make_token(newUser)
            # })
            
            # email = EmailMessage(
            #     email_subject,
            #     message2,
            #     settings.EMAIL_HOST_USER,
            #     [newUser.email]
            # )
            # email.fail_silently = True
            # email.send()
            # return redirect('signin')
        else:
            messages.info(request,"Your password and confirm password do not match!!!")
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = auth.authenticate(username = username,password = pass1)
        
        if user is not None:
            auth.login(request, user)
            name = user.first_name
            return render(request,'index.html' )
        
        else:
            messages.error(request, "User Not Found")
            return render(request,'signin.html')
    else:
        return render(request,'signin.html')

def signout(request):
    auth.logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('/')

# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         newUser = User.objects.get(pk=uid)
    
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         newUser = None
    
#     if newUser is not None and generate_token.check_token(newUser, token):
#         newUser.is_active = True
#         newUser.save()
#         login(request,newUser)
#         return redirect('home')
#     else:
#         return render(request,'activation_failed.html')
# Create your views here.


def faculty_papers_view(request):
    # user is authenticated or not
    if request.user.is_authenticated:
        email = request.POST.get('email')  # Assuming email is passed via query parameter
        name = request.POST.get('name') # Assuming Author name is provided via query parameter
        # papers = [{
        # "title":"Pyton",
        # "authors":"Von",
        # "publication_date":"10-02-1990"
        # },
        # {
        # "title":"Python",
        # "authors":"Von",
        # "publication_date":"10-02-1990"
        # }]
        papers = get_papers_by_author_id(email,name)
        return render(request, 'papers.html', {'papers': papers})
    else:
        return render(request,'signin.html' )

