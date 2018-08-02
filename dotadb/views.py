from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.http import HttpResponseRedirect
from .forms import ReplayForm

from .models import Replay
from .forms import ReplayForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ReplayForm(request.POST, request.FILES)
        if form.is_valid():
            replay = Replay(replayfile=request.FILES['files'])
            replay.save()
            return HttpResponseRedirect(reverse('dotadb.views.index'))
    else:
        form = ReplayForm()

    replays = Replay.objects.all()
    return render(request, 'dotadb/index.html', {'replays' : replays, 'form' : form})



def list(request):
    replays = Replay.objects.all()
    return render(request,'dotadb/list.html', {'replays': replays})



def handle_replay(replay):
    with open('filename', 'wb+') as destination:
        for chunk in f.chunks() :
            destination.write(chunk)