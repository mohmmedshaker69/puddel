# Generated by Django 5.0 on 2024-01-04 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0003_rename_category_item_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Convesetion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modefied_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convesetion', to='item.item')),
                ('members', models.ManyToManyField(related_name='convesetion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modefied_at',),
            },
        ),
        migrations.CreateModel(
            name='ConvesetionMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('convesetion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='convesetion.convesetion')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
