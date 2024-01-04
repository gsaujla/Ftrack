from django.shortcuts import render ,redirect
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    profile = Profile.objects.filter( user = request.user ).first()
    if request.method == 'POST':
        obtained_text = request.POST.get("descp")
        obtained_amount = request.POST.get("amount")
        nature = request.POST.get("Bool")
        
        new_activity = activity(user = request.user ,description = obtained_text , amount = obtained_amount , gain = nature)
        new_activity.save()
        print(nature)

        if nature is True:
            profile.balance += float(obtained_amount)
            
        else:
            profile.balance -= float(obtained_amount)
            profile.expenditure  += float(obtained_amount)
            
        profile.save()
        return redirect('/')
             



    
    return render(request,'tracker/index.html',{'profile' : profile})

