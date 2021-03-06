# Generated by Django 3.0.5 on 2020-04-15 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('size', models.IntegerField()),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balls', to='catalog.Player')),
            ],
        ),
    ]
