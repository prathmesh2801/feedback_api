# Generated by Django 5.1.2 on 2024-10-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('subject', models.CharField(max_length=250)),
                ('questions', models.TextField()),
            ],
        ),
    ]
