# Generated by Django 5.2.3 on 2025-06-16 17:10

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
                ('title', models.CharField(max_length=200)),
                ('opening_crawl', models.TextField()),
                ('director', models.CharField(max_length=100)),
                ('producers', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('climate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('movies', models.ManyToManyField(related_name='characters', to='starwars.movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='planets',
            field=models.ManyToManyField(related_name='movies', to='starwars.planet'),
        ),
    ]
