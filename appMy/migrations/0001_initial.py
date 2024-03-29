# Generated by Django 4.2.8 on 2024-01-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='Haber')),
                ('date_now', models.DateField(verbose_name='Tarih')),
                ('author', models.CharField(max_length=50, verbose_name='Yazar')),
            ],
        ),
    ]
