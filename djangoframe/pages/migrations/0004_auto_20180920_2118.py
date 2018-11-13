# Generated by Django 2.1.1 on 2018-09-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_article_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
