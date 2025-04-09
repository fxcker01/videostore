from django.shortcuts import render

def custom_403_view(request, exception=None):
    return render(request, "errors/403.html", status=403)