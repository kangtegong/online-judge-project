from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
#from homework.models import Course

Group_select = (
    ("Student", "Student"),
    ("Professor", "Professor"),
    ("Guest", "Guest")
)

class MyUser(AbstractUser, models.Model):
    group = models.CharField(max_length=10, choices=Group_select, default="Guest")
    phone = PhoneNumberField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to="user_images")
    myclass = models.ManyToManyField("homework.Course", blank= True)
    realname = models.CharField(max_length=20, blank=True, null=True)
    # mycode = models.URLField(blank=True, null=True)

class UserCode(models.Model):
    title = models.CharField(max_length=100) 
    user = models.ForeignKey("accounts.MyUser", on_delete=models.CASCADE, null=True)
    mycode = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
