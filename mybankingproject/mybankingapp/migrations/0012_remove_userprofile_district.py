# Generated by Django 4.2.7 on 2023-11-24 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybankingapp', '0011_rename_district_district_name_remove_branch_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='district',
        ),
    ]
