# Generated by Django 4.2.8 on 2024-01-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_comment_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Kategori')),
                ('slug', models.SlugField(verbose_name='')),
            ],
        ),
    ]
