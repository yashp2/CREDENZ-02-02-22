# Generated by Django 2.2.6 on 2021-12-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0003_alter_rcquestion_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rcplayer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rcquestion',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rcsubmission',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rctestcase',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
