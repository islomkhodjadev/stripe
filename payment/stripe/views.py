from django.shortcuts import render

# Create your views here.


def index(request):
    
    context = {
        
    }
    
    return render(request, "stripe/payment.html", context=context)
    