# Generated by Django 3.2.3 on 2021-12-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rcquestion',
            name='language',
            field=models.CharField(choices=[('c', 'C'), ('cpp', 'C++'), ('py', 'Python')], max_length=10, null=True),
        ),
    ]