from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#from accounts.models import MyUser
from django.urls import reverse

class FreePost(models.Model):
    author = models.ForeignKey("accounts.MyUser", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100) 
    body = RichTextUploadingField(blank=True, null=True)
    # code = RichTextUploadingField(blank=True, null=True, config_name='special')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
    
    class Meta:
        ordering = ['-created_at',]
