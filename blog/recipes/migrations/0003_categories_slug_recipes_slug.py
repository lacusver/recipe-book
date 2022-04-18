# Generated by Django 4.0.3 on 2022-04-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipelist_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='recipes',
            name='slug',
            field=models.SlugField(max_length=150, null=True, unique=True),
        ),
    ]