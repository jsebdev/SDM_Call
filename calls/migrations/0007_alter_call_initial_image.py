# Generated by Django 4.1.7 on 2023-02-15 15:24

import calls.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0006_rename_generatedimage_call_generated_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='initial_image',
            field=models.ImageField(blank=True, null=True, upload_to=calls.utils.get_image_path),
        ),
    ]
