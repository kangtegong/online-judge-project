from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가
from .models import FreePost
from hitcount.views import HitCountDetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = '/'

    model = FreePost
    paginate_by = 10

class PostCreate(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'

    model = FreePost
    fields = ['title', 'body',]
    success_url = reverse_lazy('freeboardlist')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

class PostDetail(LoginRequiredMixin, HitCountDetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = FreePost
    count_hit = True 

class PostUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = '/'
    model = FreePost
    fields = ['title', 'body']
    success_url = reverse_lazy('freeboardlist')

class PostDelete(LoginRequiredMixin, DeleteView):
    login_url = '/'
    redirect_field_name = '/'
    model = FreePost
    success_url = reverse_lazy('freeboardlist')
