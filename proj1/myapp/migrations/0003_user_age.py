# Generated by Django 4.2.10 on 2024-03-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_id_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]