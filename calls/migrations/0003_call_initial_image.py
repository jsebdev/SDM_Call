# Generated by Django 4.1.7 on 2023-02-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_alter_call_model_alter_call_prompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='initial_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
