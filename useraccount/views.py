from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from useraccount.forms import CustomSignUpForm,ProfileForm
from useraccount.models import Profile
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def login_view(request):

    form = AuthenticationForm(request.POST or None)
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {user}.")
            return HttpResponseRedirect(reverse("bmi:bmi_list"))
        if request.user.is_authenticted():
            return render(request,"list.html")
        else:
            form = AuthenticationForm(request.POST)
            return render(reequest,"login.html",{"form":form})
    else:
            form = AuthenticationForm(request.POST)
            return render(request,"login.html",{"form":form})
        # else:
		#     messages.error(request,"Invalid username or password.")
    context = { "form": form}
    return render(request,"login.html",context)

class UserLogin(LoginView):

    template_name = "login.html"
    # form_class = AuthenticationForm  //for  custom login
    redirect_authenticated_user = True  # By default False

def logout_view(request):
    logout(request)
    messages.info(request,"You have successfully logged out.")
    return redirect("user:login")

def signup_view(request):
    form = CustomSignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user : login"))
    context = { "form" : form }
    return render(request,"register.html",context)

def send_confirm_email(request):
    subject = "Test Subject"
    message = "Test Message"
    from_email = "shahram6154@gmail.com"
    reciepient_list = ["saugatbasnet5@gmail.com","shakya.saleem@gmail.com",]
    context = { "name" : "Saugat" }
    html_message = render_to_string("email.html", context)
    result = send_mail(subject, message, from_email, reciepient_list, html_message=html_message)
    return HttpResponse(result)

def profile_list(request):
    profiles = Profile.objects.all()
    context = { "profiles":profiles }
    return render(request,"userlist.html",context)

def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse("user:user_list"))
    context = { "form" : form }
    return render(request,"profile.html",context)

def edit_profile(request,id):
    profile = get_object_or_404(Profile, id=id)
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:user_list"))
    context = { "form":form }
    return render(request,"profile.html",context)

def delete_profile(request,id):
    profile = get_object_or_404(Profile, id=id)
    profile.delete()
    return HttpResponseRedirect(reverse("user:user_list"))

