from django.shortcuts import render

# Create your views here.

def allfriends (request):
    namelist=['shanks','nishcal','krits','aayush','Mojha','kops','Anjis']
    d={
        'names' : namelist
    }
    return render(request,"friend_app/all.html",d)
