from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def portfolio(request):
    return render(request,'portfolio.html')
def service(request):
    return render(request,'service.html')
def single(request):
    return render(request,'single.html')
def team(request):
    return render(request,'team.html')
def login(request):
    return render(request,'login.html')


