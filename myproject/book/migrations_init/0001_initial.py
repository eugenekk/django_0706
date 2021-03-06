# Generated by Django 3.2.5 on 2021-07-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=15)),
            ],
        ),
    ]
