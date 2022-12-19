# Generated by Django 4.1.4 on 2022-12-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='githubLink',
            field=models.URLField(default='https://www.geeksforgeeks.org / charfield-django-models/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.TextField(),
        ),
    ]
