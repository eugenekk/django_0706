# Generated by Django 3.2.5 on 2021-07-06 05:12

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sales',
            field=models.IntegerField(default=0, validators=[book.models.numCheck]),
            preserve_default=False,
        ),
    ]
