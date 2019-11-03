from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from accounts.models import MyUser, UserCode
from .models import Questions
from django.urls import reverse_lazy

# Create your views here.

class ProbView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = '/'
    model = Questions
    paginate_by = 10
    template_name = "questions_list.html"


@login_required(login_url='/')
def ftz(request):
    return render(request, 'ftz.html')

class CodeSave(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'

    model = UserCode
    fields = ['title', 'mycode', ]
    success_url = reverse_lazy('ftz')
    template_name = 'codesave.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    
