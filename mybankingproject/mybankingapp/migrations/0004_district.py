# Generated by Django 4.2.7 on 2023-11-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybankingapp', '0003_alter_branch_name_alter_userprofile_account_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
