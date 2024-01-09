# Generated by Django 3.2.21 on 2024-01-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_contact_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-email'],
            },
        ),
    ]
