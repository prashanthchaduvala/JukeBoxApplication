# Generated by Django 3.2 on 2021-06-21 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=80)),
                ('Date_of_release', models.DateField(auto_now=True)),
                ('genre', models.CharField(choices=[('Classic', 'Classic'), ('Pop', 'Pop'), ('Western', 'Western'), ('Melody', 'Melody')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('music_type', models.CharField(choices=[('Vilon', 'Vilon'), ('Piano', 'Piano'), ('Drums', 'Drums'), ('Flute', 'Flute')], max_length=10)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicapp.album')),
            ],
        ),
    ]
