# Generated by Django 5.0 on 2024-01-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convesetion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='convesetionmessage',
            name='content',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]
