# Generated by Django 5.0.6 on 2024-07-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0026_rename_username_customuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
