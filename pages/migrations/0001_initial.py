# Generated by Django 4.1.dev20211217120704 on 2022-01-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='courses/')),
                ('authorimage', models.ImageField(upload_to='courses/authors')),
            ],
        ),
    ]
