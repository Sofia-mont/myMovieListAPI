# Generated by Django 4.1.6 on 2023-02-06 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('dateBirth', models.DateField()),
                ('placeBirth', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('dateBirth', models.DateField()),
                ('placeBirth', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='movies')),
                ('country', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('release', models.DateField()),
                ('cast', models.ManyToManyField(to='movies.actors')),
                ('directer_by', models.ManyToManyField(to='movies.directors')),
                ('genres', models.ManyToManyField(to='movies.genres')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'db_table': 'movies',
            },
        ),
    ]
