# Generated by Django 4.0.5 on 2022-06-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mixxo_model',
            fields=[
                ('mixxo_key', models.IntegerField(primary_key=True, serialize=False)),
                ('mixxo_image', models.TextField()),
                ('mixxo_link', models.TextField()),
            ],
            options={
                'db_table': 'mixxo',
            },
        ),
        migrations.CreateModel(
            name='spao_model',
            fields=[
                ('spao_key', models.IntegerField(primary_key=True, serialize=False)),
                ('spao_image', models.TextField()),
                ('spao_link', models.TextField()),
            ],
            options={
                'db_table': 'spao',
            },
        ),
    ]