from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

Note_CHOICES = (
    (True, "학과공지"),
    (False, "학생회공지"),
    (None, "기타공지")
)

class Notice(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True)
    by_whom = models.NullBooleanField(blank=False, choices = Note_CHOICES)
    date = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.title
    
# api <-- 학사공지 : 제목(title) 날짜(date) 본문(body) / 학사달력 : 날짜(date), 내용(title)

class ExtraCurricular(models.Model):
    title = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True)
    expiration_date = models.DateTimeField()
    