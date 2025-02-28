# Generated by Django 3.2.10 on 2021-12-16 23:58

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20211216_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='yarn',
            name='length',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='yarn',
            name='weight',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='content',
            field=markdownx.models.MarkdownxField(null=True),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='use_needle_size',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='use_season',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
