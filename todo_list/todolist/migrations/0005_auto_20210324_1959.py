# Generated by Django 3.1.7 on 2021-03-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20210324_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='24-03-2021'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='24-03-2021'),
        ),
    ]
