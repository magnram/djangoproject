# Generated by Django 2.1.1 on 2018-10-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_articlecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
