from django.shortcuts import render

# Create your views here.
def index(request):
    context = {};
    return render(request, 'mixpay/index.html', context)

def settings(request):
    return render(request, 'mixpay/settings.html')
