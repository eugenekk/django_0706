# Generated by Django 3.2.5 on 2021-07-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ip',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]