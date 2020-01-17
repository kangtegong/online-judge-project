# User Model
기존 django User Model을 `AbstractUser`로 확장하여 
group, image, myclass, realname column 추가
```
accounts/models.py.

class MyUser(AbstractUser, models.Model):
    group = models.CharField(max_length=10, choices=Group_select, default="Guest")
    image = models.ImageField(null=True, upload_to="user_images")
    myclass = models.ManyToManyField("homework.Course", blank= True)
    realname = models.CharField(max_length=20, blank=True, null=True)

```
# Authentication

`from django.contrib.auth import views as auth_views`를 이용한 
로그인, 로그아웃, 회원가입 기능 구현

```
accounts/urls.py/

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='register/index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]

```

# 회원가입 

`LoginView`와 `LogoutView`는 지정된 html로 렌더링 되므로,
views.py 에는 회원가입 form 처리 로직만 지정하면 된다

```
def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register/registration_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()

    return render(request, 'register/register.html', {'form':user_form})
```