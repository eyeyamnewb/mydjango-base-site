from django.shortcuts import render, redirect


# Create your views here.
def introduction(request):
    return render(request, 'introduction.html')




