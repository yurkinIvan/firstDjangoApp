# Generated by Django 3.0.3 on 2020-03-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_comment_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_descriprion',
            field=models.CharField(default='Здесь будет описание статьи', max_length=450, verbose_name='Описание статьи'),
            preserve_default=False,
        ),
    ]
