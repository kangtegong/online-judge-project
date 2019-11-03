from django.shortcuts import render, get_object_or_404
import requests
import json
from django.contrib.auth.decorators import login_required
from board.models import FreePost
from homework.models import Assignment
from .models import Notice
from accounts.models import MyUser, UserCode
from .models import Notice

@login_required
def news(request):
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)    
    return render(request, 'news.html', {'api':api})

@login_required(login_url='/')
def index(request):
    notice = Notice.objects.all()
    assignments = Assignment.objects.all()
    return render(request, 'dash.html', {'notice':notice, 'assignments':assignments})

@login_required(login_url='/')
def test(request):
    return render(request, 'test.html')

@login_required(login_url='/')
def note(request):
    notes = Notice.objects.all()
    return render(request, 'note.html', {'notes':notes})

def note_detail(request, note_pk):
    note = get_object_or_404(Notice, pk=note_pk)
    return render(request, 'note-detail.html', {'note': note})

## user page ## 

@login_required(login_url='/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/')
def myclass(request):
    return render(request, 'myclass.html')

@login_required(login_url='/')
def calendar(request):
    return render(request, 'calendar.html')

@login_required(login_url='/')
def mycode(request):
    codes = UserCode.objects.all()
    return render(request, 'mycode.html', {'codes':codes})
