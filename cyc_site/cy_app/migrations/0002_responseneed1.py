# Generated by Django 4.1.2 on 2022-12-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cy_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responseneed1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('passwo', models.CharField(max_length=50)),
            ],
        ),
    ]
