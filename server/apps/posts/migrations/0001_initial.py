# Generated by Django 4.1.5 on 2023-02-12 21:22

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
                ('name_ru', models.CharField(max_length=50,
                 null=True, verbose_name='category name')),
                ('name_en', models.CharField(max_length=50,
                 null=True, verbose_name='category name')),
                ('name_tr', models.CharField(max_length=50,
                 null=True, verbose_name='category name')),
                ('slug', autoslug.fields.AutoSlugField(
                    editable=False, populate_from='name', unique=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('content_ru', models.TextField(null=True, verbose_name='content')),
                ('content_en', models.TextField(null=True, verbose_name='content')),
                ('content_tr', models.TextField(null=True, verbose_name='content')),
                ('created', models.DateField(
                    auto_now=True, verbose_name='creation date')),
                ('is_published', models.BooleanField(
                    default=False, verbose_name='is post published?')),
                ('read_duration', models.IntegerField(
                    default=5, verbose_name='reading duration')),
                ('thumbnail', models.ImageField(
                    upload_to='posts/thumbnail/', verbose_name='thumbnail')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_ru', models.CharField(
                    max_length=255, null=True, verbose_name='title')),
                ('title_en', models.CharField(
                    max_length=255, null=True, verbose_name='title')),
                ('title_tr', models.CharField(
                    max_length=255, null=True, verbose_name='title')),
                ('slug', autoslug.fields.AutoSlugField(
                    editable=False, populate_from='title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='posts', to='posts.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='tag name')),
                ('name_ru', models.CharField(max_length=50,
                 null=True, verbose_name='tag name')),
                ('name_en', models.CharField(max_length=50,
                 null=True, verbose_name='tag name')),
                ('name_tr', models.CharField(max_length=50,
                 null=True, verbose_name='tag name')),
                ('slug', autoslug.fields.AutoSlugField(
                    editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(
                    max_length=55, verbose_name='full name')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='comments', to='posts.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(
                blank=True, related_name='posts', to='posts.tag', verbose_name='tags'),
        ),
    ]
