# Generated by Django 3.2.13 on 2022-06-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osoriapp', '0004_alter_freecomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='post_photo'),
        ),
    ]