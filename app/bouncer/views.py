from django.shortcuts import render

def landing(request):
    # 'index.html' to nazwa Twojego pliku w folderze templates
    return render(request, 'bouncer/index.html')