from django.shortcuts import redirect


def redirect_site(request):
    redirect('/', permanent=True)