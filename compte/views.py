from django.shortcuts import render

# Create your views here.

app_name = "compte"


def signup_view(request):
    return render(request, "compte/signup.html")
