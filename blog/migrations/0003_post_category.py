# Generated by Django 3.1.7 on 2021-03-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('ai', 'AI'), ('capitalism', 'CAPITALISM'), ('creative writing', 'CREATIVE WRITING')], default='ai', max_length=20),
        ),
    ]
