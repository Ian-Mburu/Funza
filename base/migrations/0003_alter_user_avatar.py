# Generated by Django 5.1.1 on 2024-10-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='cat.png', null=True, upload_to=''),
        ),
    ]
