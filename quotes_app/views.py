from django.shortcuts import render

# Create your views here.
def allquotes(request):
    feature=['drink one glass of water every day']
    d={
        'quoname': feature
    }
    return render(request,'quotes_app/quo.html',d)
