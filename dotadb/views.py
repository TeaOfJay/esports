from django.shortcuts import render

# Create your views here.

def upload_replay(request):
    if request.method == 'POST':
        #handle POST    