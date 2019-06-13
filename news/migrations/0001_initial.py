# Generated by Django 2.1.4 on 2019-06-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('description', models.TextField(default='', max_length=340, verbose_name='Краткое описание')),
                ('image', models.ImageField(blank=True, default='../static\\images\\logo.png', upload_to='../media/images', verbose_name='Изображение')),
                ('create', models.DateTimeField(verbose_name='Создано')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('moder', models.BooleanField(default=False, verbose_name='Модерация')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'article',
                'ordering': ['-create'],
            },
        ),
    ]