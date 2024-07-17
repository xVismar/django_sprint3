# Generated by Django 3.2.16 on 2024-07-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Время создания записи.', verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Время создания записи.', verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Время создания записи.', verbose_name='Добавлено'),
        ),
    ]