# Generated by Django 4.0.5 on 2022-06-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hooda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
