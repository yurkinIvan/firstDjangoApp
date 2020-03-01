# Generated by Django 3.0.3 on 2020-03-01 14:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200229_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 1, 14, 58, 10, 271983, tzinfo=utc), verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]