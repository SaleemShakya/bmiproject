from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse,get_object_or_404
from calculator.models import Bmi,Suggestion
from calculator.forms import BmiForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.

def suggest(request):
    suggests = Suggestion.objects.all()
    context = { "suggests":suggests }
    return render(request,"suggest.html",context)

    if bmi <= 18.5:
        print("Your are underweight")

    elif bmi <= 24.9:
        print("You are normal")

    elif bmi <= 29.9:
        print("Your are overweight")

    elif bmi <= 30.0:
        print("Your are obsessed")
        
@login_required  
def bmi_list(request):
    # bmis = Bmi.objects.all()
    bmis = Bmi.objects.filter(user=request.user)
    context = { "bmis":bmis }
    return render(request,"list.html",context)

@login_required
def bmi_add(request):
    # if request.method == "POST":
    form = BmiForm(request.POST or None)
    if form.is_valid():
        height = form.cleaned_data["height"]
        weight = form.cleaned_data["weight"]
        bmi = weight / height**2
        if bmi <= 18.5:
            messages.warning(request,"Under Weight")
        elif 18.5 < bmi < 24.9:
            messages.success(request,"Normal Weight")
        elif 25.0 < bmi < 30.0:
            messages.info(request,"Over Weight")
        elif bmi > 30.0:
            messages.error(request,"Obssesed Weight")
        return render(request,"form.html",{"bmi":bmi})
        bmi = form.save(commit=False)
        bmi.user = request.user
        form.save()
        return HttpResponseRedirect(reverse("bmi:bmi_list"))
    context = { "form":form }
    return render(request,"form.html",context)

@login_required
@permission_required
def bmi_edit(request,id):
    bmi = get_object_or_404(Bmi,id=id)
    form = BmiForm(request.POST or None,instance=bmi)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("bmi:bmi_list"))
    context = { "form":form }
    # return HttpResponse(id)
    return render(request, "form.html", context)

@login_required
def bmi_delete(request, id):
    bmi = get_object_or_404(Bmi,id=id)
    bmi.delete()
    return HttpResponseRedirect(reverse("bmi:bmi_list"))


