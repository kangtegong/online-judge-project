from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가
from .models import Course, Assignment, CodeSubmit, FileSubmit
from .forms import HWForm, FileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def hwlist(request, pk):
    course = get_object_or_404(Course, pk=pk)
    assignments = course.assignment_set.all()

    return render(request, 'homework/hw_list.html', {'assignments': assignments})

class CourseList(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = '/'
    model = Course
    
class HWCreate(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'
    model = Assignment
    form_class = HWForm
    #fields = ['class_div', 'expiration_date', 'title', 'body']
    success_url = reverse_lazy('courselist')

class HWDetail(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = Assignment

@login_required(login_url='/')
def codereview(request):
    homework = Assignment.objects.all()
    return render(request, 'homework/code.html', {'homework':homework})

class CodeSubmits(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'
    model = CodeSubmit
    fields = ['assignment', 'title', 'codeurl', 'code' ]
    template_name = 'homework/code-submit.html'
    success_url = reverse_lazy('courselist')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    
        
class FileSubmits(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'
    model = FileSubmit
    template_name = 'homework/file.html'
    fields = ['assignment','title', 'myfile', 'body']
    success_url = reverse_lazy('courselist')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

class MailSubmits(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = '/'
    model = CodeSubmit
    fields = '__all__'
    template_name = 'homework/mail.html'
    success_url = reverse_lazy('courselist')

@login_required(login_url='/')
def submitlist(request, pk):
    # 넘어오는 pk값은 Assignment의 pk
    # 특정 pk 값에 해당하는 과제만 내보내고 싶은데 흠
    # Assignment의 pk가 있고 FileSubmit, CodeSubmit의 pk
    assignment = get_object_or_404(Assignment, pk=pk)
    submitfiles = FileSubmit.objects.all()
    codefiles = CodeSubmit.objects.all()
    
    return render(request, 'homework/submissions.html', {
        'assignment': assignment, 
        'submitfiles':submitfiles, 
        'codefiles':codefiles
        })
    
'''
class SubmitList(ListView):
    context_object_name = 'submitfiles'    # 제출 과제 object 이름
    template_name = 'homework/submissions.html'
    queryset = FileSubmit.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SubmitList, self).get_context_data(**kwargs)
        context['codefiles'] = CodeSubmit.objects.all() 
        context['assignment'] = Assignment.objects.all()
        return context
'''
class ClassRegister(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = '/'
    template_name = 'homework/classregister.html'
    model = Course

@login_required(login_url='/')
def registerclass(request, pk):
    # 이걸 누르면 누른 사용자의 user.myclass에 해당하는 수업을 추가하면 되는 거
    myclass = get_object_or_404(Course, pk=pk)
    allclass = request.user.myclass.add(myclass)
    #all_class = allclass.objects.all()
    
    return render(request, 'homework/register-complete.html')

class FileDetail(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = FileSubmit
    template_name = "homework/file-detail.html"

class CodeDetail(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = '/'
    model = CodeSubmit
    template_name = "homework/code-detail.html"



