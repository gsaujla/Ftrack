from django.shortcuts import render ,redirect , get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    expense = activity.objects.filter(user= request.user)
    Profile = profile.objects.filter( user = request.user ).first()
    if request.method == 'POST':
        obtained_text = request.POST.get("descp")
        obtained_amount = request.POST.get("amount")
        nature = request.POST.get("gain")
        
        new_activity = activity(user = request.user ,description = obtained_text , amount = obtained_amount , gainornot = nature)
        new_activity.save()
        print(nature)
        
        if nature == "Yes":
            Profile.balance += float(obtained_amount)
            print("I am a gain of" + str(obtained_amount))
            Profile.save()
            return redirect('/')
            
        elif nature == "No":
            Profile.balance -= float(obtained_amount)
            Profile.expenditure  += float(obtained_amount)
            print("deducted")
            Profile.save()
            return redirect('/')

          
            
        
             



    
    return render(request,'tracker/index.html',{'Profile' : Profile , 'expense' : expense})

