# Generated by Django 3.2.4 on 2021-07-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_pizza_name', models.CharField(blank=True, max_length=200, verbose_name='Pizza du jour')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('price', models.FloatField(default=0.0, verbose_name='Prix')),
                ('image', models.ImageField(upload_to='photos/daily_pizza')),
                ('ingredients', models.TextField(max_length=500)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Pizza du jour',
                'verbose_name_plural': 'Pizza du jour',
            },
        ),
    ]