# Generated by Django 4.2.8 on 2024-01-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_alter_sessionyearmodel_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstaff',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
