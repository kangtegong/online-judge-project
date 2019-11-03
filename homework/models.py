from django.db import models
#from accounts.models import MyUser
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Course(models.Model):
    subject_no = models.CharField(max_length=20, blank=True, primary_key=True)           # 교과번호
    class_div = models.CharField(max_length=20, blank=True)               # 분반
    subject_nm = models.CharField(max_length=40, blank=True)              # 교과목명
    shyr = models.CharField(max_length=20, blank=True)                    # 학년
    prof_nm = models.CharField(max_length=20, blank=True)                 # 담당교수
    class_nm = models.CharField(max_length=50, blank=True, null=True)                # 강의시간및강의실

    def __str__(self):
        return self.subject_nm

    class Meta:
        ordering = ['-subject_no',]

class Assignment(models.Model):

    HW_CHOICES = (
        ("CODE", "코딩과제"),
        ("FILE", "제출과제"),
    )

    class_choice = models.ForeignKey(Course, on_delete = models.CASCADE, null=True)
    class_div = models.PositiveSmallIntegerField(default=1,blank=True, null=True )               
    expiration_date = models.DateTimeField()
    hw_type = models.CharField(max_length=10, choices=HW_CHOICES,default="CODE")
    title = models.CharField(max_length=30, blank=True) 
    body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at',]

class CodeSubmit(models.Model):
    author = models.ForeignKey("accounts.MyUser", on_delete=models.CASCADE, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100) 
    code = RichTextUploadingField(blank=True, null=True, config_name='special')
    codeurl = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at',]

class FileSubmit(models.Model):
    author = models.ForeignKey("accounts.MyUser", on_delete=models.CASCADE, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100) 
    myfile = models.FileField(null=True, blank=True, upload_to='file_submit/%Y/%m/%d/')
    body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at',]

