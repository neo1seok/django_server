# Generated by Django 2.2.3 on 2019-07-11 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_report', '0002_table2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table2',
            name='author',
        ),
    ]