# Generated by Django 5.1.4 on 2024-12-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='posters/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=100)),
                ('main_actors', models.CharField(help_text='הפרד את שמות השחקנים בפסיקים', max_length=200)),
                ('year_of_release', models.PositiveIntegerField()),
            ],
        ),
    ]
