# Generated by Django 4.2.5 on 2023-10-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_delete_postpage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
