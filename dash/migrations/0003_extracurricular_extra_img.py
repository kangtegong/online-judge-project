# Generated by Django 2.0 on 2019-11-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_extracurricular'),
    ]

    operations = [
        migrations.AddField(
            model_name='extracurricular',
            name='extra_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]