# Generated by Django 3.2.10 on 2021-12-16 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_yarn_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='yarn',
            old_name='manufacturer_name',
            new_name='manufacturer',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='yarn',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.yarn')),
            ],
        ),
    ]
