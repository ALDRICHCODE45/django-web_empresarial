# Generated by Django 5.0.7 on 2024-08-04 07:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]