# Generated by Django 4.2.8 on 2024-01-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='Ad - Soyad')),
                ('comment', models.TextField(verbose_name='Yorum')),
            ],
        ),
    ]
