# Generated by Django 5.0.4 on 2024-04-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.EmailField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
