# Generated by Django 2.0 on 2019-09-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190830_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='group',
            field=models.CharField(choices=[('Student', 'Student'), ('Professor', 'Professor'), ('Guest', 'Guest')], default='Guest', max_length=10),
        ),
    ]
